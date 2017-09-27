#include<stdio.h>
#include "TFile.h"
#include "TCanvas.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TF1.h"
#include "TF2.h"
#include "TLeaf.h"
#include "TMath.h"
#include "TTree.h"
#include "TLegend.h"
#include "TPaveText.h"

Int_t countBits(Int_t word);

Float_t windowAlignment = 1000; // in ns (cut signal and background)
Float_t windowAlignment2 = 10000; // in ns (cut signal and background)

// (1)
// setting for histos
const Int_t nbint = 100;
const Float_t tmin = -10000; //ns
const Float_t tmax = 10000; //ns
const Float_t maxwidth = 400;

// (2)
// periods
Int_t yearRange[2] = {2014,2017};
Int_t monthRange[2] = {11,12};
Int_t dayRange[2] = {1,1};

// thresholds for good runs
Int_t hitevents[2] = {10000,10000};
Float_t fracGT[2] = {0.8,0.8};
Float_t rateMin[2] = {10,10};
Float_t rateMax[2] = {70,70};

// old cut on the missing rate (replaced by the number of dead strips)
Float_t minmissingHitFrac[2] = {-1,-1};
Float_t maxmissingHitFrac[2] = {1,1};

// number of deadstrips allowed
Int_t ndeadBotMax[2] = {23,23};
Int_t ndeadBotMin[2] = {0,0};
Int_t ndeadMidMax[2] = {23,23};
Int_t ndeadMidMin[2] = {0,0};
Int_t ndeadTopMax[2] = {23,23};
Int_t ndeadTopMin[2] = {0,0};

// requirement on the number of satellites in the run (average)
Float_t minAvSat[2] = {0.,0.};
Float_t maxAvSat[2] = {10,10};

// time difference between weather info and the start of the run (it is negative!) allowed (in seconds)
Int_t minWeathTimeDelay[2] = {-999999,-999999};
Int_t maxWeathTimeDelay[2] = {3600,3600};

// experiment to autocorrect for efficiency variation
Float_t refRate[2] = {23,23};

// (3)
// thresholds for good events
Float_t maxchisquare = 10*10/2;
Float_t minthetarel = 0;
Float_t maxthetarel = 60;
Int_t satEventThr = 0; // minimum number of sattellite required in each event

// (4)
// telescope settings
Float_t angle = 85.75; //deg
Float_t distance=1075;

Float_t deltatCorr = 0; // knows shift in gps time difference for a given pair of telescopes (bolo ~ 1500)
// extra corrections
Bool_t recomputeThetaRel = kTRUE; // if true correction below are applied to adjust the phi angles of the telescopes
Float_t phi1Corr = 27; // in degrees (the one stored in the header + refinements)
Float_t phi2Corr = 297; // in degrees

void doCoincTORI_03_04new(const char *fileIn="coincTORI_0304n.root"){

  // Print settings
  printf("SETTINGS\nAnalyze output from new Analyzer\n");
  printf("Input file = %s\n",fileIn);
  printf("School distance = %f m, angle = %f deg\n",distance,angle);
  printf("School orientation: tel1=%f deg, tel2=%f deg\n",phi1Corr,phi2Corr);
  printf("Max Chi2 = %f\n",maxchisquare);
  printf("Theta Rel Range = %f - %f deg\n",minthetarel,maxthetarel);
  printf("Range for N sattellite in each run = (tel1) %f - %f, (tel2) %f - %f \n",minAvSat[0],maxAvSat[0],minAvSat[1],maxAvSat[1]);
  printf("Min N satellite in a single event = %i\n",satEventThr);

  Int_t adayMin = (yearRange[0]-2014) * 1000 + monthRange[0]*50 + dayRange[0];
  Int_t adayMax = (yearRange[1]-2014) * 1000 + monthRange[1]*50 + dayRange[1];

  Float_t nsigPeak=0;
  Float_t nbackPeak=0;

  angle *= TMath::DegToRad();

  // define some histos
  TH1F *hDeltaTheta = new TH1F("hDeltaTheta","#Delta#theta below the peak (500 ns);#Delta#theta (#circ)",100,-60,60);
  TH1F *hDeltaPhi = new TH1F("hDeltaPhi","#Delta#phi below the peak (500 ns);#Delta#phi (#circ)",200,-360,360);
  TH1F *hDeltaThetaBack = new TH1F("hDeltaThetaBack","#Delta#theta out of the peak (> 1000 ns) - normalized;#Delta#theta (#circ)",100,-60,60);
  TH1F *hDeltaPhiBack = new TH1F("hDeltaPhiBack","#Delta#phi out of the peak (> 1000 ns)  - normalized;#Delta#phi (#circ)",200,-360,360);
  TH1F *hThetaRel = new TH1F("hThetaRel","#theta_{rel} below the peak (500 ns);#theta_{rel} (#circ)",100,0,120);
  TH1F *hThetaRelBack = new TH1F("hThetaRelBack","#theta_{rel} out of the peak (> 1000 ns)  - normalized;#theta_{rel} (#circ)",100,0,120);

  TH2F *hAngle = new TH2F("hAngle",";#Delta#theta (#circ);#Delta#phi (#circ}",20,-60,60,20,-360,360);
  TH2F *hAngleBack = new TH2F("hAngleBack",";#Delta#theta (#circ);#Delta#phi (#circ}",20,-60,60,20,-360,360);

  TProfile *hModulation = new  TProfile("hModulation","#theta^{rel} < 10#circ;#phi - #alpha;dist (m)",50,0,360);
  TProfile *hModulation2 = new  TProfile("hModulation2","#theta^{rel} < 10#circ;#phi - #alpha;dist (m)",50,0,360);
  TProfile *hModulationAv = new  TProfile("hModulationAv","#theta^{rel} < 10#circ;#phi - #alpha;dist (m)",50,0,360);
  TProfile *hModulationAvCorr = new  TProfile("hModulationAvCorr","#theta^{rel} < 10#circ;#phi - #alpha;diff (ns)",50,0,360);

  TH1F *hnsigpeak = new TH1F("hnsigpeak","",50,0,360);
  TH1F *hnbackpeak = new TH1F("hnbackpeak","",50,0,360);

  TProfile *hSinTheta = new  TProfile("hSinTheta",";#phi - #alpha;sin(#theta)",50,0,360);
  TProfile *hSinTheta2 = new  TProfile("hSinTheta2",";#phi - #alpha;sin(#theta)",50,0,360);

  TH1F *hRunCut[2];
  hRunCut[0] = new TH1F("hRunCut1","Reason for Run Rejection Tel-1;Reason;runs rejected",11,0,11);
  hRunCut[1] = new TH1F("hRunCut2","Reason for Run Rejection Tel-2;Reason;runs rejected",11,0,11);

  for(Int_t i=0;i<2;i++){
    hRunCut[i]->Fill("DateRange",0);
    hRunCut[i]->Fill("LowFractionGT",0);
    hRunCut[i]->Fill("TimeDuration",0);
    hRunCut[i]->Fill("rateGT",0);
    hRunCut[i]->Fill("RunNumber",0);
    hRunCut[i]->Fill("MissingHitFrac",0);
    hRunCut[i]->Fill("DeadStripBot",0);
    hRunCut[i]->Fill("DeadStripMid",0);
    hRunCut[i]->Fill("DeadStripTop",0);
    hRunCut[i]->Fill("NSatellites",0);
    hRunCut[i]->Fill("NoGoodWeather",0);  
  }

  TFile *f = new TFile(fileIn);
  TTree *t = (TTree *) f->Get("tree");
  
  TTree *tel[2];
  tel[0] = (TTree *) f->Get("treeTel1");
  tel[1] = (TTree *) f->Get("treeTel2");
  
  TTree *telC = (TTree *) f->Get("treeTimeCommon");
  
  // quality info of runs
  const Int_t nyearmax = 5;
  Bool_t runstatus[2][nyearmax][12][31][500]; //#telescope, year-2014, month, day, run
  Float_t effTel[2][nyearmax][12][31][500];
  Int_t nStripDeadBot[2][nyearmax][12][31][500];
  Int_t nStripDeadMid[2][nyearmax][12][31][500];
  Int_t nStripDeadTop[2][nyearmax][12][31][500];

  Float_t nstripDeadB[2]={0,0},nstripDeadM[2]={0,0},nstripDeadT[2]={0,0};
 
  // sat info
  Float_t NsatAv[2][nyearmax][12][31][500];

  // weather info
  Float_t pressureTel[2][nyearmax][12][31][500];
  Float_t TempInTel[2][nyearmax][12][31][500];
  Float_t TempOutTel[2][nyearmax][12][31][500];
  Float_t timeWeath[2][nyearmax][12][31][500];

  Float_t rateGT;

  Float_t phirelative;
  Float_t phirelative2;
  Float_t phirelativeAv;

  printf("Check Run quality\n");

  if(tel[0] && tel[1]){
    for(Int_t i=0;i < 2;i++){ // loop on telescopes
      printf("Tel-%i\n",i+1);
      for(Int_t j=0;j < tel[i]->GetEntries();j++){ // loop on runs
	tel[i]->GetEvent(j);
	rateGT = tel[i]->GetLeaf("FractionGoodTrack")->GetValue()*tel[i]->GetLeaf("rateHitPerRun")->GetValue();

	Int_t aday = (tel[i]->GetLeaf("year")->GetValue()-2014) * 1000 + tel[i]->GetLeaf("month")->GetValue()*50 + tel[i]->GetLeaf("day")->GetValue();

	if(aday < adayMin || aday > adayMax){
	  hRunCut[i]->Fill("DateRange",1); continue;}
	if(tel[i]->GetLeaf("FractionGoodTrack")->GetValue() < fracGT[i]){
	  hRunCut[i]->Fill("LowFractionGT",1); continue;} // cut on fraction of good track
	if(tel[i]->GetLeaf("timeduration")->GetValue()*tel[i]->GetLeaf("rateHitPerRun")->GetValue() < hitevents[i]){
	  hRunCut[i]->Fill("TimeDuration",1); continue;} // cut on the number of event
	if(rateGT < rateMin[i] || rateGT > rateMax[i]){
	  hRunCut[i]->Fill("rateGT",1); continue;} // cut on the rate
	if(tel[i]->GetLeaf("run")->GetValue() > 499){
	  hRunCut[i]->Fill("RunNumber",1); continue;} // run < 500

	Float_t missinghitfrac = (tel[i]->GetLeaf("ratePerRun")->GetValue()-tel[i]->GetLeaf("rateHitPerRun")->GetValue()-2)/(tel[i]->GetLeaf("ratePerRun")->GetValue()-2);
	if(missinghitfrac < minmissingHitFrac[i] || missinghitfrac > maxmissingHitFrac[i]){
	  hRunCut[i]->Fill("MissingHitFrac",1); continue;}
		
	// active strip maps
	if(tel[i]->GetLeaf("maskB")) nStripDeadBot[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] = countBits(Int_t(tel[i]->GetLeaf("maskB")->GetValue()));
	if(tel[i]->GetLeaf("maskM")) nStripDeadMid[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] = countBits(Int_t(tel[i]->GetLeaf("maskM")->GetValue()));
	if(tel[i]->GetLeaf("maskT")) nStripDeadTop[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] = countBits(Int_t(tel[i]->GetLeaf("maskT")->GetValue()));

	if(nStripDeadBot[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] > ndeadBotMax[i] || nStripDeadBot[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] < ndeadBotMin[i]) {
	  hRunCut[i]->Fill("DeadStripBot",1); continue;}
	if(nStripDeadMid[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] > ndeadMidMax[i] || nStripDeadMid[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] < ndeadMidMin[i]){
	  hRunCut[i]->Fill("DeadStripMid",1); continue;}
	if(nStripDeadTop[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] > ndeadTopMax[i] || nStripDeadTop[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] < ndeadTopMin[i]){
	  hRunCut[i]->Fill("DeadStripTop",1); continue;}

	// nsat averaged  per run
	if(tel[i]->GetLeaf("nSat")) NsatAv[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] = tel[i]->GetLeaf("nSat")->GetValue();


	if(NsatAv[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] < minAvSat[i] || NsatAv[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] > maxAvSat[i]){
	 hRunCut[i]->Fill("NSatellites",1); continue;}

	// weather info
	if(tel[i]->GetLeaf("Pressure")) pressureTel[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] = tel[i]->GetLeaf("Pressure")->GetValue();
	if(tel[i]->GetLeaf("IndoorTemperature")) TempInTel[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] = tel[i]->GetLeaf("IndoorTemperature")->GetValue();
	if(tel[i]->GetLeaf("OutdoorTemperature")) TempOutTel[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] = tel[i]->GetLeaf("OutdoorTemperature")->GetValue();
	if(tel[i]->GetLeaf("TimeWeatherUpdate")) timeWeath[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] = tel[i]->GetLeaf("TimeWeatherUpdate")->GetValue();

	if(timeWeath[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] < minWeathTimeDelay[i] ||  timeWeath[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] > maxWeathTimeDelay[i]){
	  hRunCut[i]->Fill("NoGoodWeather",1); continue;}

	// Set good runs
	runstatus[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] = kTRUE;
	effTel[i][Int_t(tel[i]->GetLeaf("year")->GetValue())-2014][Int_t(tel[i]->GetLeaf("month")->GetValue())][Int_t(tel[i]->GetLeaf("day")->GetValue())][Int_t(tel[i]->GetLeaf("run")->GetValue())] = 1;//rateGT/refRate[i];
      }
    }
  }
  else{
    telC = NULL;
  }
  printf("Start to process correlations\n");
  Int_t n = t->GetEntries();

  // counter for seconds
  Int_t nsec = 0;
  Int_t nsecGR = 0; // for good runs
  Int_t isec = -1; // used only in case the tree with time info is not available

  Float_t neventsGR = 0;
  Float_t neventsGRandSat = 0;

  if(telC){
    for(Int_t i=0; i < telC->GetEntries();i++){
      telC->GetEvent(i);
      nsec += telC->GetLeaf("timeduration")->GetValue(); 
      
      
      
      if(telC->GetLeaf("run")->GetValue() > 499 || telC->GetLeaf("run2")->GetValue() > 499) continue;
      
      if(!runstatus[0][Int_t(telC->GetLeaf("year")->GetValue())-2014][Int_t(telC->GetLeaf("month")->GetValue())][Int_t(telC->GetLeaf("day")->GetValue())][Int_t(telC->GetLeaf("run")->GetValue())]) continue;
      
      if(!runstatus[1][Int_t(telC->GetLeaf("year")->GetValue())-2014][Int_t(telC->GetLeaf("month")->GetValue())][Int_t(telC->GetLeaf("day")->GetValue())][Int_t(telC->GetLeaf("run2")->GetValue())]) continue;
      
      nsecGR += telC->GetLeaf("timeduration")->GetValue(); 
      nstripDeadB[0] += countBits(nStripDeadBot[0][Int_t(telC->GetLeaf("year")->GetValue())-2014][Int_t(telC->GetLeaf("month")->GetValue())][Int_t(telC->GetLeaf("day")->GetValue())][Int_t(telC->GetLeaf("run")->GetValue())])*telC->GetLeaf("timeduration")->GetValue();
      nstripDeadM[0] += countBits(nStripDeadMid[0][Int_t(telC->GetLeaf("year")->GetValue())-2014][Int_t(telC->GetLeaf("month")->GetValue())][Int_t(telC->GetLeaf("day")->GetValue())][Int_t(telC->GetLeaf("run")->GetValue())])*telC->GetLeaf("timeduration")->GetValue();
      nstripDeadT[0] += countBits(nStripDeadTop[0][Int_t(telC->GetLeaf("year")->GetValue())-2014][Int_t(telC->GetLeaf("month")->GetValue())][Int_t(telC->GetLeaf("day")->GetValue())][Int_t(telC->GetLeaf("run")->GetValue())])*telC->GetLeaf("timeduration")->GetValue();

      nstripDeadB[1] += countBits(nStripDeadBot[1][Int_t(telC->GetLeaf("year")->GetValue())-2014][Int_t(telC->GetLeaf("month")->GetValue())][Int_t(telC->GetLeaf("day")->GetValue())][Int_t(telC->GetLeaf("run")->GetValue())])*telC->GetLeaf("timeduration")->GetValue();
      nstripDeadM[1] += countBits(nStripDeadMid[1][Int_t(telC->GetLeaf("year")->GetValue())-2014][Int_t(telC->GetLeaf("month")->GetValue())][Int_t(telC->GetLeaf("day")->GetValue())][Int_t(telC->GetLeaf("run")->GetValue())])*telC->GetLeaf("timeduration")->GetValue();
      nstripDeadT[1] += countBits(nStripDeadTop[1][Int_t(telC->GetLeaf("year")->GetValue())-2014][Int_t(telC->GetLeaf("month")->GetValue())][Int_t(telC->GetLeaf("day")->GetValue())][Int_t(telC->GetLeaf("run")->GetValue())])*telC->GetLeaf("timeduration")->GetValue();
    }
    nstripDeadB[0] /= nsecGR;
    nstripDeadM[0] /= nsecGR;
    nstripDeadT[0] /= nsecGR;

    nstripDeadB[1] /= nsecGR;
    nstripDeadM[1] /= nsecGR;
    nstripDeadT[1] /= nsecGR;

    printf("Dead channel tel1 = %f - %f - %f\n",nstripDeadB[0],nstripDeadM[0],nstripDeadT[0]);
    printf("Dead channel tel2 = %f - %f - %f\n",nstripDeadB[1],nstripDeadM[1],nstripDeadT[1]);
  }
  
  char title[300];
  TH1F *h;
  
  sprintf(title,"correction assuming #Delta#phi = %4.2f, #DeltaL = %.1f m;#Deltat (ns);entries",angle,distance);
  
  h = new TH1F("hCoinc",title,nbint,tmin,tmax);
  
  Float_t DeltaT;
  Float_t phiAv,thetaAv,corr;
  
  Float_t Theta1,Theta2;
  Float_t Phi1,Phi2;
  Int_t nsatel1cur,nsatel2cur,ntrack1,ntrack2;

  Float_t v1[3],v2[3],vSP; // variable to recompute ThetaRel on the fly
  Float_t eff = 1; 
  
  for(Int_t i=0;i<n;i++){
    t->GetEvent(i);
    
    if(t->GetLeaf("RunNumber1") && (t->GetLeaf("RunNumber1")->GetValue() > 499 || t->GetLeaf("RunNumber2")->GetValue() > 499)) continue;
  
    if(tel[0] && !runstatus[0][Int_t(t->GetLeaf("year")->GetValue())-2014][Int_t(t->GetLeaf("month")->GetValue())][Int_t(t->GetLeaf("day")->GetValue())][Int_t(t->GetLeaf("RunNumber1")->GetValue())]) continue;
    
    if(tel[1] && !runstatus[1][Int_t(t->GetLeaf("year")->GetValue())-2014][Int_t(t->GetLeaf("month")->GetValue())][Int_t(t->GetLeaf("day")->GetValue())][Int_t(t->GetLeaf("RunNumber2")->GetValue())]) continue;


    eff = effTel[0][Int_t(t->GetLeaf("year")->GetValue())-2014][Int_t(t->GetLeaf("month")->GetValue())][Int_t(t->GetLeaf("day")->GetValue())][Int_t(t->GetLeaf("RunNumber1")->GetValue())];
    eff *= effTel[1][Int_t(t->GetLeaf("year")->GetValue())-2014][Int_t(t->GetLeaf("month")->GetValue())][Int_t(t->GetLeaf("day")->GetValue())][Int_t(t->GetLeaf("RunNumber2")->GetValue())];
    
    Int_t timec = t->GetLeaf("ctime1")->GetValue();
    
    if(! telC){
      if(isec == -1) isec = timec;
      
      if(timec != isec){
	if(timec - isec < 20){
	  //	printf("diff = %i\n",timec-isec);
	  nsec +=(timec - isec);
	  nsecGR +=(timec - isec);
	}
	isec = timec;
    }
    }

    Float_t thetarel = t->GetLeaf("ThetaRel")->GetValue();
    Theta1 = (t->GetLeaf("Theta1")->GetValue())*TMath::DegToRad();
    Theta2 = t->GetLeaf("Theta2")->GetValue()*TMath::DegToRad();
    Phi1 = t->GetLeaf("Phi1")->GetValue()*TMath::DegToRad();
    Phi2 = t->GetLeaf("Phi2")->GetValue()*TMath::DegToRad();
    
    nsatel1cur = t->GetLeaf("Nsatellite1")->GetValue();
    nsatel2cur = t->GetLeaf("Nsatellite2")->GetValue();
    ntrack1 = t->GetLeaf("Ntracks1")->GetValue();
    ntrack2 = t->GetLeaf("Ntracks2")->GetValue();

    if(recomputeThetaRel){ // recompute ThetaRel applying corrections
      Phi1 += phi1Corr*TMath::DegToRad();
      Phi2 += phi2Corr*TMath::DegToRad();
      if(Phi1 > 2*TMath::Pi()) Phi1 -= 2*TMath::Pi();
      if(Phi1 < 0) Phi1 += 2*TMath::Pi();
      if(Phi2 > 2*TMath::Pi()) Phi2 -= 2*TMath::Pi();
      if(Phi2 < 0) Phi2 += 2*TMath::Pi();
      
      v1[0] = TMath::Sin(Theta1)*TMath::Cos(Phi1);
      v1[1] = TMath::Sin(Theta1)*TMath::Sin(Phi1);
      v1[2] = TMath::Cos(Theta1);
      v2[0] = TMath::Sin(Theta2)*TMath::Cos(Phi2);
      v2[1] = TMath::Sin(Theta2)*TMath::Sin(Phi2);
      v2[2] = TMath::Cos(Theta2);
      
      v1[0] *= v2[0];
      v1[1] *= v2[1];
      v1[2] *= v2[2];
      
      vSP = v1[0] + v1[1] + v1[2];
      
      thetarel = TMath::ACos(vSP)*TMath::RadToDeg();
    }
    
    // cuts
    if(thetarel < minthetarel) continue;
    if(thetarel > maxthetarel) continue;
    if(t->GetLeaf("ChiSquare1")->GetValue() > maxchisquare) continue;
    if(t->GetLeaf("ChiSquare2")->GetValue() > maxchisquare) continue;
    

    neventsGR++;

    // reject events with not enough satellites
    if(nsatel1cur < satEventThr || nsatel1cur < satEventThr) continue;

    neventsGRandSat++;
    
    DeltaT = t->GetLeaf("DiffTime")->GetValue();
    
    // get primary direction
    if(TMath::Abs(Phi1-Phi2) < TMath::Pi()) phiAv = (Phi1+Phi2)*0.5;
    else phiAv = (Phi1+Phi2)*0.5 + TMath::Pi();

    thetaAv = (Theta1+Theta2)*0.5;
    
    // extra cuts if needed
    //    if(TMath::Cos(Phi1-Phi2) < 0.) continue;
    
    Float_t resFactor = 1;
    if(thetarel > 10 ) resFactor *= 0.5;
    if(thetarel > 20 ) resFactor *= 0.5;
    if(thetarel > 30 ) resFactor *= 0.5;

    corr = distance * TMath::Sin(thetaAv)*TMath::Cos(phiAv-angle)/2.99792458000000039e-01 + deltatCorr;

    phirelative = (Phi1-angle)*TMath::RadToDeg();
    if(phirelative < 0) phirelative += 360;
    if(phirelative < 0) phirelative += 360;
    if(phirelative > 360) phirelative -= 360;
    if(phirelative > 360) phirelative -= 360;

    phirelative2 = (Phi2-angle)*TMath::RadToDeg();
    if(phirelative2 < 0) phirelative2 += 360;
    if(phirelative2 < 0) phirelative2 += 360;
    if(phirelative2 > 360) phirelative2 -= 360;
    if(phirelative2 > 360) phirelative2 -= 360;

    phirelativeAv = (phiAv-angle)*TMath::RadToDeg();
    if(phirelativeAv < 0) phirelativeAv += 360;
    if(phirelativeAv < 0) phirelativeAv += 360;
    if(phirelativeAv > 360) phirelativeAv -= 360;
    if(phirelativeAv > 360) phirelativeAv -= 360;


    // if(TMath::Abs(DeltaT- deltatCorr) < windowAlignment){
      
    // }

    if(thetarel < 10){//cos(thetarel*TMath::DegToRad())>0.98 && sin(thetaAv)>0.1){
      if(TMath::Abs(DeltaT- corr) < windowAlignment2)
	hModulationAvCorr->Fill(phirelativeAv,DeltaT-corr);
      if(TMath::Abs(DeltaT- deltatCorr) < windowAlignment2){
	hModulation->Fill(phirelative,(DeltaT-deltatCorr)/sin(thetaAv)*2.99792458000000039e-01);
	hModulation2->Fill(phirelative2,(DeltaT-deltatCorr)/sin(thetaAv)*2.99792458000000039e-01);
	hModulationAv->Fill(phirelativeAv,(DeltaT-deltatCorr)/sin(thetaAv)*2.99792458000000039e-01);
	hSinTheta->Fill(phirelative,sin(thetaAv));
	hSinTheta2->Fill(phirelative2,sin(thetaAv));
	nsigPeak++;
	hnsigpeak->Fill(phirelativeAv);
      }
      else if(TMath::Abs(DeltaT- deltatCorr) < windowAlignment2*10){
	nbackPeak++;
	hnbackpeak->Fill(phirelativeAv);
      }
    }

    h->Fill(DeltaT-corr,1./eff);
    if(TMath::Abs(DeltaT-corr) < windowAlignment){
      hDeltaTheta->Fill((Theta1-Theta2)*TMath::RadToDeg());
      hDeltaPhi->Fill((Phi1-Phi2)*TMath::RadToDeg());
      hThetaRel->Fill(thetarel);
      hAngle->Fill((Theta1-Theta2)*TMath::RadToDeg(),(Phi1-Phi2)*TMath::RadToDeg());
    }
    else if(TMath::Abs(DeltaT-corr) > windowAlignment*2 && TMath::Abs(DeltaT-corr) < windowAlignment*12){
      hDeltaThetaBack->Fill((Theta1-Theta2)*TMath::RadToDeg());
      hDeltaPhiBack->Fill((Phi1-Phi2)*TMath::RadToDeg());
      hThetaRelBack->Fill(thetarel);
      hAngleBack->Fill((Theta1-Theta2)*TMath::RadToDeg(),(Phi1-Phi2)*TMath::RadToDeg());
    }
  }
  
  // compute (S+B)/S
  for(Int_t i=1;i<=50;i++){
    Float_t corrfactorPeak = 1;
    if(nsigPeak-nbackPeak*0.1 > 0)
      corrfactorPeak = hnsigpeak->GetBinContent(i)/(hnsigpeak->GetBinContent(i)-hnbackpeak->GetBinContent(i)*0.1);
    else
      printf("bin %i) not enough statistics\n",i);
    hnsigpeak->SetBinContent(i,corrfactorPeak);
  }

  TF1 *fpol0 = new TF1("fpol0","pol0");
  hnsigpeak->Fit(fpol0);

  if(fpol0->GetParameter(0) > 0) hModulation->Scale(fpol0->GetParameter(0));
  if(fpol0->GetParameter(0) > 0) hModulation2->Scale(fpol0->GetParameter(0));
  if(fpol0->GetParameter(0) > 0) hModulationAv->Scale(fpol0->GetParameter(0));
  if(fpol0->GetParameter(0) > 0) hModulationAvCorr->Scale(fpol0->GetParameter(0));
  
  TF1 *fmod = new TF1("fmod","[0] + [1]*cos((x-[2])*TMath::DegToRad())"); 
  hModulationAv->Fit(fmod); 

  printf("Estimates from time delay: Distance = %f +/- %f m -- Angle = %f +/- %f deg\n",fmod->GetParameter(1),fmod->GetParError(1),fmod->GetParameter(2),fmod->GetParError(2));

  h->SetStats(0);

  hDeltaThetaBack->Sumw2();
  hDeltaPhiBack->Sumw2();
  hThetaRelBack->Sumw2();
  hDeltaThetaBack->Scale(0.1);
  hDeltaPhiBack->Scale(0.1);
  hThetaRelBack->Scale(0.1);
  hAngleBack->Scale(0.1);
  hAngle->Add(hAngleBack,-1);

  printf("bin counting: SIGNAL = %f +/- %f\n",hDeltaPhi->Integral()-hDeltaPhiBack->Integral(),sqrt(hDeltaPhi->Integral()));


  Float_t val,eval;
  TCanvas *c1=new TCanvas();
  TF1 *ff = new TF1("ff","[0]*[4]/[2]/sqrt(2*TMath::Pi())*TMath::Exp(-(x-[1])*(x-[1])*0.5/[2]/[2]) + [3]*[4]/6/[2]");
  ff->SetParName(0,"signal");
  ff->SetParName(1,"mean");
  ff->SetParName(2,"sigma");
  ff->SetParName(3,"background");
  ff->SetParName(4,"bin width");
  ff->SetParameter(0,42369);
  ff->SetParameter(1,0);
  ff->SetParLimits(2,200,maxwidth);
  ff->SetParameter(2,350); // fix witdh if needed
  ff->SetParameter(3,319);
  ff->FixParameter(4,(tmax-tmin)/nbint); // bin width

  ff->SetNpx(1000);
  
  h->Fit(ff,"EI","",-10000,10000);
  
  val = ff->GetParameter(2);
  eval = ff->GetParError(2);
  
  printf("significance = %f\n",ff->GetParameter(0)/sqrt(ff->GetParameter(0) + ff->GetParameter(3)));

  h->Draw();
  
  TF1 *func1 = (TF1 *)  h->GetListOfFunctions()->At(0);
  
  func1->SetLineColor(2);
  h->SetLineColor(4);
  
  TPaveText *text = new TPaveText(1500,(h->GetMinimum()+(h->GetMaximum()-h->GetMinimum())*0.6),9500,h->GetMaximum());
  text->SetFillColor(0);
  sprintf(title,"width = %5.1f #pm %5.1f",func1->GetParameter(2),func1->GetParError(2));
  text->AddText(title);
  sprintf(title,"signal (S) = %5.1f #pm %5.1f",func1->GetParameter(0),func1->GetParError(0));
  text->AddText(title);
  sprintf(title,"background (B) (3#sigma) = %5.1f #pm %5.1f",func1->GetParameter(3),func1->GetParError(3));
  text->AddText(title);
  sprintf(title,"significance (S/#sqrt{S+B}) = %5.1f",func1->GetParameter(0)/sqrt(func1->GetParameter(0)+func1->GetParameter(3)));
  text->AddText(title);
  
  text->SetFillStyle(0);
  text->SetBorderSize(0);
  
  text->Draw("SAME");
  
  // correct nsecGR for the event rejected because of the number of satellites (event by event cut)
  nsecGR *= neventsGRandSat/neventsGR;

  printf("n_day = %f\nn_dayGR = %f\n",nsec*1./86400,nsecGR*1./86400);

  text->AddText(Form("rate = %f #pm %f per day",func1->GetParameter(0)*86400/nsecGR,func1->GetParError(0)*86400/nsecGR));

  TFile *fo = new TFile("outputTORI-03-04.root","RECREATE");
  h->Write();
  hDeltaTheta->Write();
  hDeltaPhi->Write();
  hThetaRel->Write();
  hDeltaThetaBack->Write();
  hDeltaPhiBack->Write();
  hThetaRelBack->Write();
  hAngle->Write();
  hModulation->Write();
  hModulation2->Write();
  hModulationAv->Write();
  hModulationAvCorr->Write();
  hSinTheta->Write();
  hSinTheta2->Write();
  hnsigpeak->Write();
  hRunCut[0]->Write();
  hRunCut[1]->Write();
  fo->Close();
  
}

Int_t countBits(Int_t word){
  Int_t nactive = 0;
  while (word > 0) {           // until all bits are zero
    if ((word & 1) == 1)     // check lower bit
      nactive++;
    word >>= 1;              // shift bits, removing lower bit
  }
  return nactive;
}

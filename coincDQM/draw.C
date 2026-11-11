void draw(const char *in,const char *out,Float_t dist,const char *macro,const char *last="",Float_t ndays=1,Float_t ratemin=0,Int_t secLastFile=0){
  TTimeStamp ts;

  TFile *f = new TFile(in);
  TCanvas *c1= new TCanvas();
  if(!tree->GetEntriesFast()) return;
//  tree->Draw("DiffTime >>htemp(50,-10000,10000)","TMath::Abs(DiffTime) < 10000");

  gROOT->LoadMacro(macro);
  Float_t rate,rateErr;
  Int_t expndays = ndays;

  ndays = doCoinc(in,c1,rate,rateErr);

  char filetrend[200];
  sprintf(filetrend,"%s",out);
  filetrend[15] = '\0';
  char title[500];
  sprintf(title,"Trending for %s;date;rate (coinc/day)",filetrend);

  char pair[200];
  sprintf(pair,"%s",filetrend);

  sprintf(filetrend,"%s.trend",filetrend);


  system(Form("echo %i %f %f>tmp ",ts.GetSec(),rate,rateErr));
  system(Form("cat tmp %s > tmp2; mv tmp2 %s",filetrend,filetrend));  

  c1->cd();
  hCoinc->SetTitle(Form("for %.1f days, (last %s), d=%.0f m;#Deltat (ns);N",ndays,last,dist));
  hCoinc->SetStats(0);
//  hCoinc->SetMinimum(0);
  c1->Print(out);
  system(Form("cp %s /home/analisi/dqmcoincidences/",out));

  FILE *ft = fopen(filetrend,"r");
  Int_t ninfo=0;
  Float_t x[100],ex[100],y[100],ey[100];
  Int_t sec;
  Float_t val,errval;
  while(fscanf(ft,"%i %f %f",&sec,&val,&errval) == 3 && ninfo < 30){
    x[ninfo] = sec;
    ex[ninfo] = 0;
    y[ninfo] = val;
    ey[ninfo] = errval;
    ninfo++;
  } 

  c1->cd();
  TGraphErrors *g = new TGraphErrors(ninfo,x,y,ex,ey);
  g->Draw("AP");
  g->SetMarkerStyle(20);
  g->GetXaxis()->SetTimeDisplay(1);
  g->GetXaxis()->SetTimeFormat("%d-%m-%y%F1970-01-01 00:00:00s0");
  g->GetXaxis()->SetNdivisions(408);
  g->SetMinimum(TMath::Min(-ey[0],y[0]));
  g->SetTitle(title);

  TLine *l = new TLine(x[0],0,x[ninfo-1],0);

  l->SetLineColor(2);
  l->Draw("SAME");

  TLine *l2 = new TLine(x[0],ratemin,x[ninfo-1],ratemin);

  l2->SetLineColor(4);
  l2->Draw("SAME");


  c1->Print(Form("%s.png",filetrend));
  system(Form("cp %s.png /home/analisi/dqmcoincidences/",filetrend));

  fclose(ft);

  Int_t errorRate=0;
  if(rate < ratemin) errorRate++;
  if(rate + 2*rateErr < ratemin) errorRate++;

  Int_t errorDate=0;
  if(secLastFile > 86400*2) errorDate++;
  if(secLastFile > 86400*9) errorDate++;
  if(expndays > 4*ndays && errorDate < 2) errorDate++;

  printf("Rate =%f - RateMin = %f\n",rate,ratemin);
  printf("Status: ErrRate ErrDate\n");
  printf("Status:   %3i     %3i  \n",errorRate,errorDate);

  system(Form("echo %s %s %i %.1f %.1f %.1f %i > summary%s.txt",pair,last,errorDate,rate,rateErr,ratemin,errorRate,pair));
}

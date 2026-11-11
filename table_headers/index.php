<!DOCTYPE HTML>  
<html>
<head>
</head>
<body>  

<h2>Inserisci il messaggio relativo al tuo telescopio</h2>
<form action="report_action.php" method="post">
Scegli il nome del tuo telescopio:
  <select name="school">
   <option selected disabled>Scegli il telescopio</option>
   <option value="ALTA-01">ALTA-01</option>
   <option value="AREZ-01">AREZ-01</option>
   <option value="BARI-01">BARI-01</option>
   <option value="BOLO-01">BOLO-01</option>
   <option value="BOLO-02">BOLO-02</option>
   <option value="BOLO-03">BOLO-03</option>
   <option value="BOLO-04">BOLO-04</option>
   <option value="BOLO-05">BOLO-05</option>
   <option value="CAGL-01">CAGL-01</option>
   <option value="CAGL-02">CAGL-02</option>
   <option value="CAGL-03">CAGL-03</option>
   <option value="CARI-01">CARI-01</option>
   <option value="CATA-01">CATA-01</option>
   <option value="CATA-02">CATA-02</option>
   <option value="CATZ-01">CATZ-01</option>
   <option value="CERN-01">CERN-01</option>
   <option value="CERN-02">CERN-02</option>
   <option value="COSE-01">COSE-01</option>
   <option value="FRAS-01">FRAS-01</option>
   <option value="FRAS-02">FRAS-02</option>
   <option value="FRAS-03">FRAS-03</option>
   <option value="GROS-01">GROS-01</option>
   <option value="GROS-02">GROS-02</option>
   <option value="LAQU-01">LAQU-01</option>
   <option value="LAQU-02">LAQU-02</option>
   <option value="LECC-01">LECC-01</option>
   <option value="LECC-02">LECC-02</option>
   <option value="LECC-03">LECC-03</option>
   <option value="LODI-01">LODI-01</option>
   <option value="LODI-02">LODI-02</option>
   <option value="PARM-01">PARM-01</option>
   <option value="PATE-01">PATE-01</option>
   <option value="PISA-01">PISA-01</option>
   <option value="REGG-01">REGG-01</option>
   <option value="ROMA-01">ROMA-01</option>
   <option value="ROMA-02">ROMA-02</option>
   <option value="SALE-01">SALE-01</option>
   <option value="SAVO-01">SAVO-01</option>
   <option value="SAVO-02">SAVO-02</option>
   <option value="SAVO-03">SAVO-03</option>
   <option value="TERA-01">TERA-01</option>
   <option value="TORI-02">TORI-02</option>
   <option value="TORI-03">TORI-03</option>
   <option value="TORI-04">TORI-04</option>
   <option value="TRAP-01">TRAP-01</option>
   <option value="TREV-01">TREV-01</option>
   <option value="TRIN-01">TRIN-01</option>
   <option value="VIAR-01">VIAR-01</option>
   <option value="VIAR-02">VIAR-02</option>
  </select>
  <br><br>
  Inserisci il testo del messaggio: 
  <input type="text" size="50" maxlength="200" name="msg">
  <br><br>
  <input type="submit" name="submit" value="Submit">  
</form>
<p>
Il messaggio inserito verr&agrave; scritto 
nel report di EEE tutti i giorni.
</p><p>
Per togliere un messaggio gi&agrave; inserito,
basta sottomettere un messaggio vuoto (i.e. scegli il nome del tuo telescopio,
e premi il pulsante submit, senza scrivere nulla nel campo del messaggio).
</p><p>
Il messaggio che scrivi verr&agrave; letto
dal software automatico <a href="https://github.com/centrofermi/e3monitor">e3report</a>
alle ore 8:00 del mattino.
</p><p>
Esempi di messaggio (nel testo non occorre specificare il nome del proprio telescopio):
<ul>
<li>telescopio spento in attesa del gas.
<li>problema hardware da capire.
<li>si &egrave; interrotta la connessione internet della scuola, il telescopio &egrave;
in acquisizione correttamente.
<li>il gas &egrave; finalmente arrivato e il telescopio ha ripreso a funzionare.
<li>...
</ul>
</p>

</body>
</html>


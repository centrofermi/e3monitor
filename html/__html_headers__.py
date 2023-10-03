# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 18:48:52 2014

@author: Fabrizio Coccetti
"""
HEADER_HTML = """
<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="author" content="Fabrizio Coccetti" />
<meta name="generator" content="e3monitor" />
<meta http-equiv="refresh" content="60" />
<link rel="apple-touch-icon" sizes="180x180" href="./favicon/apple-touch-icon.png" />
<link rel="icon" type="image/png" sizes="32x32" href="./favicon/favicon32.png" />
<link rel="icon" type="image/png" sizes="16x16" href="./favicon/favicon16.png" />
<link rel="manifest" href="./site.webmanifest" />
<link rel="shortcut icon" href="./favicon/favicon.ico" />
<title>EEE Monitor -
Museo Storico della Fisica e Centro Studi e Ricerche Enrico Fermi</title>
<link rel="stylesheet" type="text/css"
href="https://fonts.googleapis.com/css?family=Ubuntu:regular,bold&subset=Latin">
<link href="e3monitor.css" rel="stylesheet" type="text/css" />
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-60373730-1', 'auto');
  ga('send', 'pageview');

</script>
</head>
<body>
<div id="page-wrap">
"""

PAGE_TITLE_HTML = """
<div class="flex">
<img src="img/logo_centrofermi.png" alt="Logo Centro Fermi" style="width:200px">
<div class='title'>
<h2><i>Progetto Extreme Energy Events - La Scienza nelle Scuole</i></h2>
<h1>EEE MONITOR - DQM</h1>
<div style="font-size:16px;font-style:italic;text-align:center;">[ Official address: http://eee.centrofermi.it/monitor ]</div>
</div>
<img src="img/logo_EEE.png" alt="Logo Centro Fermi" style="width:200px">
</div>
"""

TABELLA0_HTML = """
<!-- <div id="menu"> -->
<table style="table-layout:auto;width:1000px;border-collapse:separate;">
<tbody style="width:100%">
<tr>
<td style="width:700px">
"""
#<!-- <div id="menu"> -->
#<div class="flex">
#<div style="max-width:700px">

TABELLA1_HTML = """
<table>
<tr><td>

<div style="text-align: center;">
<div class="flex">
<div class="buttons">
<!--
<a href="http://eee.centrofermi.it/elog/Run6">
SCHOOLs ELOGBOOK for RUN 6</a>
<a href="http://eee.centrofermi.it/elog/Telescopes">
Telescope ELOGBOOK</a>
<a href="https://sites.google.com/centrofermi.it/3etech/">
EEE Tech Coord</a>
</div></div>
<div class="flex">
<div class="buttons">
<a href="http://eee.centrofermi.it/monitor/report/">
Set Automatic Shift REPORT Messages
</a>
<a href="http://eee.centrofermi.it/monitor/run5reports/">
Automatic Shift Report ARCHIVE</a>
</div></div>
<div class="flex">
<div class="buttons">
<a href="http://eee.centrofermi.it/">
Home Page EEE</a>
<a href="http://eee.centrofermi.it/monitor/supermonitor/run5/">
Run 5 SuperSummary</a>
<a href="https://iatw.cnaf.infn.it/eee/monitor/shifter_report.xlsx">
Download the Excel Sheet</a>
</div></div>
<div class="flex">
<div class="buttons">
<a href="https://iatw.cnaf.infn.it/eee/monitor/coincidences.html">
Coincidences</a>
<a href="http://eee.centrofermi.it/monitor/traffic">
Connectivity Report</a>
-->
<a href="https://iatw.cnaf.infn.it/eee/elog/Run7/"><b>ELOG RUN7</b></a>
</div></div>
</div></div>
<a href="http://eee.centrofermi.it/elog/Query"><b>DATA REQUEST</b></a>
</div></div>
</div>
</tr></table>
"""

PAGE_SUBTILE_HTML = '<h2><i>[EEE Monitor] RUN 6 - Data Taking - Day number: '

TABELLA1_P2_HTML = """
<!-- School Table -->
<div style="overflow-x:auto">
<table>
<tr><th>School</th>
<th>Day</th>
<th>Time</th>
<th class="small">Name of the last<br />trasferred File</th>
<th class="small">Number of Files<br />trasferred today</th>
<th class="small">Name of the last<br />File analyzed<br />by DQM</th>
<th>DQM<br />daily<br />report</th>
<th class="small">RATE of<br />Triggers<br />
for the<br />last Run<br />in DQM</th>
<th class="small">RATE of<br />Tracks<br />
for the<br />last Run<br />in DQM</th>
<th>Link DQM</th></tr>
"""
# tolto dalla tabella precedente dopo "transferred today"
#<th class="small">Last Entry<br />in the e-logbook<br />of the Schools</th>

TABELLA2_HTML = """
<div id="menu">
<table>
<tr class='gray'>
<td><a href="http://eee.centrofermi.it/elog/EEE+e-log">
ELOGBOOK delle SCUOLE</a>
</td><td>
<a href="http://eee.centrofermi.it/elog/Shifter">
ELOGBOOK dello SHIFTER</a>
</td><td>
<a href="index.html">
EEE Main Monitoring Table</B></a>
</td></tr></table>
</div>

<h2>Ultimo riscontro positivo di comunicazione tra le Scuole<br />
e il server di raccolta dati al CNAF</h2>

<p>Questa tabella pu&ograve; essere usata per verificare
se ci sono problemi di collegamento tra la propria Scuola e il CNAF.</br />
In <span class="bold">verde</span> sono indicate le Scuole in
comunicazione con il CNAF nelle ultime 2 ore.<br />
In <span class="bold">giallo</span> sono indicate le Scuole in
cui il link con  il CNAF non funziona da 3 ore.<br />
In <span class="bold">rosso</span> sono indicate le Scuole in
cui il link con il CNAF non funziona da pi&ugrave; di 3 ore.</p>
<table>
<tr><th>Scuola</th>
<th>Giorno</th
><th>Ora</th>
<th class="small">Versione<br />Software Trasferimento</th></tr>
"""

TRACK_PLOT_HTML = """
<br />
</div>
<h3 style="margin-top:24px;">Today's plot of the total number of candidate
tracks vs
months of data acquisition</h3>
<div style="text-align:center;padding:0px;margin:0px;">
<a href="plots/tracks.png">
<img src="plots/tracks.png" alt="Tracks" style="width:100%;max-width:1200px;">
</a>
</div>


<div style="font-size:80%;text-align: left;">
<table>

<tr><td class="blue">
<div style="font-size:140%; text-align: left; color: white; font-weight:bold;">
La tabella sottostante mostra la situazione dei telescopi:
</div>
</td></tr>

<tr><td class="green">
<div style="text-align: left;">
- In <span class="bold">verde</span> sono indicati i telescopi in
presa dati e trasferimento nelle ultime 3 ore
e con parametri di acquisizione ragionevoli nell'ultimo run analizzato.
</div>
</td></tr>

<tr><td class="yellow">
<div style="text-align: left;">
- In <span class="bold">giallo</span> sono indicati i telescopi in
cui trasferimento e/o acquisizione sono sospesi da pi&ugrave; di 3 ore
o con tracce (X^2&lt;10) minori di 10 Hz nell'ultimo run analizzato.
</div>
</td></tr>

<tr><td class="red">
<div style="text-align: left;">
- In <span class="bold">rosso</span> sono indicati i telescopi in
cui trasferimento e/o acquisizione sono sospesi da pi&ugrave; di due giorni
o con tracce (X^2&lt;10) minori di 5 Hz nell'ultimo run analizzato.<br />
</div>
</td></tr>

<tr><td class="gray">
<div style="text-align: left; color: black;">
- In <span class="bold">grigio</span> sono indicati i telescopi in 
attesa di ripartire con la nuova miscela di gas ecosostenibile.<br />
</div>
</td></tr>

<tr><td class="wheat">
<div style="text-align: left; color: black;">
- In <span class="bold">beige</span> sono indicati gli archivi storici dei dati
dei telescopi che ora sono stati spostati in altre scuole.
</div>
</td></tr>
</table>
</div>

</div>
</div>
</td>
<!-- <td>
<div style="width:300px; padding:0px; margin:0px; border: 1px solid #555555;">
<a class="twitter-timeline" data-lang="en" data-width="300" data-height="400" data-theme="light" href="https://twitter.com/centrofermi?ref_src=twsrc%5Etfw">Tweets by centrofermi</a> <script async src="https://platform.twitter.com/widgets.js"></script>
</div>
</td>  -->
"""

FOOTER_HTML = """
<p>&nbsp;</p>
<div id="footer">
<p>Webpage made by&nbsp;
<a href="https://github.com/centrofermi/e3monitor">e3monitor</a>&nbsp;
[<a href="https://github.com/centrofermi/e3monitor/wiki/Architecture">architecture</a>]
&nbsp;[<a href="https://github.com/centrofermi/e3monitor/wiki">wiki</a>]
"""

BOTTOM_HTML = """
</p> <!-- close paragraph in footer -->
</div> <!-- close footer -->
</div> <!-- close page-wrap -->
</body>
</html>
"""

DQM_HEADER_HTML = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="it" xml:lang="it" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<meta name="author" content="Fabrizio Coccetti" />
<meta name="generator" content="e3monitor" />
<meta http-equiv="REFRESH" content="60"/>
<meta http-equiv="Expires" content="0"/>
<meta http-equiv="PRAGMA" content="NO-CACHE"/>
<title>EEE Monitor -
Museo Storico della Fisica e Centro Studi e Ricerche Enrico Fermi</title>
<link href="favicon.ico" rel="shortcut icon" type="image/vnd.microsoft.icon" />
<link rel="stylesheet" type="text/css"
href="https://fonts.googleapis.com/css?family=Ubuntu:regular,bold&subset=Latin">
<link href="e3monitor.css" rel="stylesheet" type="text/css" />
</head>
<body>
<div id="page-wrap">
    <p style="margin-bottom:6px;">
    <img src="img/banner_centro_fermi.jpg"
    alt="banner CF" width="800" /></p>
"""

DQM_TITLE_HTML = """
<h2><i>Progetto Extreme Energy Events - La Scienza nelle Scuole</i></h2>
<h1>Coincidences DQM</h1>
"""

DQM_BOTTOM_HTML = """
</div> <!-- close page-wrap -->
</body>
</html>
"""

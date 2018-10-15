# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 18:48:52 2014

@author: Fabrizio Coccetti
"""
HEADER_HTML = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
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
<table>
<tr><td class='title'>
<img src="img/logo_centrofermi.png" alt="Logo Centro Fermi" width="200px">
</td><td class='title'>
<h2><i>Progetto Extreme Energy Events - La Scienza nelle Scuole</i></h2>
<h1>EEE MONITOR - DQM</h1>
<div style="font-size:16px;font-style:italic;">[ Official address: http://eee.centrofermi.it/monitor ]</div>
</td><td class='title'>
<img src="img/logo_EEE.png" alt="Logo Centro Fermi" width="200px">
</td></tr>
</table>
"""

TABELLA0_HTML = """
<!-- <div id="menu"> -->
<table style="table-layout:auto;width:1000px;border-collapse:separate;">
<tbody style="width:100%">
<tr>
<td style="width:700px">
"""

TABELLA1_HTML = """
<div style="text-align: left;">
<table>
<tr class='gray'>
<td><a href="http://eee.centrofermi.it/elog/Run5">
SCHOOLs ELOGBOOK for RUN 5</a>
</td><td>
<a href="http://eee.centrofermi.it/elog/Shifter">
SHIFTERs ELOGBOOK</a>
</td><td>
<a href="https://sites.google.com/centrofermi.it/3etech/">
EEE Tech Coord</a>
</td></tr></table>
<table>
<tr class='gray'>
<td>
<a href="http://eee.centrofermi.it/monitor/report/">
Set Automatic Shift REPORT Messages
</a>
</td><td>
<a href="http://eee.centrofermi.it/monitor/run5reports/">
Automatic Shift Report ARCHIVE</a>
</td></tr></table>
<table>
<tr class='gray'>
<td>
<a href="http://eee.centrofermi.it/">
Home Page EEE</a>
</td><td>
<a href="http://eee.centrofermi.it/monitor/masterclass/">
Masterclass</a>
</td><td>
<a href="https://iatw.cnaf.infn.it/eee/monitor/shifter_report.xlsx">
Download the Excel Sheet</a>
</td></tr></table>
<table>
<tr class='gray'>
<td>
<a href="https://iatw.cnaf.infn.it/eee/monitor/coincidences.html">
Coincidences</a>
</td><td>
<a href="http://eee.centrofermi.it/monitor/traffic">
Connectivity Report</a>
</td><td>
<a href="http://eee.centrofermi.it/elog/Query">Data Request</a>
</td></tr></table>
</div>
"""

PAGE_SUBTILE_HTML = '<h2><i>[EEE Monitor] RUN 5 - Data Taking - Day number: '

TABELLA1_P2_HTML = """
<div style="font-size:80%;text-align: left;">
<br />
La tabella qui sotto mostra la situazione dei telescopi in acquisizione:<br />

In <span class="bold">verde</span> sono indicati i telescopi in
presa dati e trasferimento nelle ultime 3 ore<br /> 
e con parametri di acquisizione ragionevoli nell'ultimo run analizzato.<br />

In <span class="bold">giallo</span> sono indicati i telescopi in
cui trasferimento e/o acquisizione sono sospesi da pi&ugrave; di 3 ore<br />
o con tracce (X^2<10) minori di 10 Hz nell'ultimo run analizzato.<br />

In <span class="bold">rosso</span> sono indicati i telescopi in
cui trasferimento e/o acquisizione sono sospesi da pi&ugrave; di due giorni<br />
o con tracce (X^2<10) minori di 5Hz nell'ultimo run analizzato.</div>

</td>
<td style="width:300px; padding:0px; margin:0px; border: 1px solid #555555;">
<a class="twitter-timeline" data-lang="en" data-width="300" data-height="400" data-theme="light" href="https://twitter.com/centrofermi?ref_src=twsrc%5Etfw">Tweets by centrofermi</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</td></tr></tbody></table>
<!-- Closing main twitter table -->
<table>
<tr><th>School</th>
<th>Day</th>
<th>Time</th>
<th class="small">Name of the last<br />trasferred File</th>
<th class="small">Number of Files<br />trasferred today</th>
<th class="small">Last Entry<br />in the e-logbook<br />of the Schools</th>
<th class="small">Name of the last<br />File analyzed<br />by DQM</th>
<th>DQM<br />daily<br />report</th>
<th class="small">RATE of<br />Triggers</br />
for the<br />last Run<br />in DQM</th>
<th class="small">RATE of<br />Tracks<br />
for the<br />last Run<br />in DQM</th>
<th>Link DQM</th></tr>
"""

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

FOOTER_HTML = """
<h3 style="margin-top:24px;">Today's plot of the total number of candidate tracks vs
months of data acquisition</h3>
<div style="text-align:left;padding:0px;margin:0px;">
<a href="plots/tracks.png">
<img src="plots/tracks.png" alt="Tracks" width="1200">
</a>
</div>
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

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 18:48:52 2014

@author: Fabrizio Coccetti
"""
HEADER_HTML = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<meta name="author" content="Fabrizio Coccetti" />
<meta name="generator" content="e3monitor" />
<meta http-equiv="REFRESH" content="60"/>
<meta http-equiv="Expires" content="0"/>
<meta http-equiv="PRAGMA" content="NO-CACHE"/>
<title>EEE Monitor -
Museo Storico della Fisica e Centro Studi e Ricerche Enrico Fermi</title>
<link rel="stylesheet" type="text/css"
href="https://fonts.googleapis.com/css?family=Ubuntu:regular,bold&subset=Latin">
<link href="e3monitor.css" rel="stylesheet" type="text/css" />
</head>
<body>
<div id="page-wrap">
    <p style="margin-bottom:6px;">
    <img src="http://www.centrofermi.it/docs/images/banner_centro_fermi.jpg"
    alt="banner CF" width="800" /></p>
"""

PAGE_TITLE_HTML = '<h1>Extreme Energy Events Monitor</h1>'

TABELLA1_HTML = """
<div id="menu">
<table>
<tr class='gray'>
<td><a href="http://www.centrofermi.it/elog/EEE+e-log">
ELOGBOOK delle SCUOLE</a>
</td><td>
<a href="http://www.centrofermi.it/elog/Shifter">
ELOGBOOK dello SHIFTER</a>
</td><td>
<a href="http://eee.centrofermi.it/">
Home Page EEE</a>
</td><td>
<a href="https://www.cnaf.infn.it/eee/monitor/shifter_report.xlsx">
Download the Excel Sheet for the Shifter's Report
</td></tr></table>
</div>

<h2>EEE Monitor</h2>

<p>Questa tabella mostra la situazione dei telescopi in acquisizione<br />
In <span class="bold">verde</span> sono indicati i telescopi in
presa dati e trasferimento nelle ultime 4 ore.<br />
In <span class="bold">giallo</span> sono indicati i telescopi in
cui trasferimento e/o acquisizione sono sospesi da pi&ugrave; di 4 ore.<br />
In <span class="bold">rosso</span> sono indicati i telescopi in
cui trasferimento e/o acquisizione sono sospesi da pi&ugrave; di un giorno.</p>

<table>
<tr><th>Scuola</th>
<th>Giorno</th>
<th>Ora</th>
<th class="small">Nome dell'ultimo<br />File trasferito</th>
<th class="small">Numero Files<br />trasferiti oggi</th>
<th class="small">Ultima Entry<br />nell'e-logbook<br />delle Scuole</th>
<th class="small">Nome dell'ultimo<br />File analizzato<br />dal DQM</th>
<th>Report<br />giornaliero<br />DQM</th>
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
<td><a href="http://www.centrofermi.it/elog/EEE+e-log">
ELOGBOOK delle SCUOLE</a>
</td><td>
<a href="http://www.centrofermi.it/elog/Shifter">
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
<p>&nbsp;</p>
<div id="footer">
<p>Webpage made by&nbsp;
<a href="https://github.com/centrofermi/e3monitor">e3monitor</a>&nbsp;
"""

BOTTOM_HTML = """
</p> <!-- close paragraph in footer -->
</div> <!-- close footer -->
</div> <!-- close page-wrap -->
</body>
</html>
"""

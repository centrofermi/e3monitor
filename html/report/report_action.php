<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="it" xml:lang="it" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<meta name="author" content="Fabrizio Coccetti" />
<meta name="Fabrizio Coccetti" content="http://www.fc8.net">
<meta name="generator" content="e3monitor" />
<title>EEE Report -
Museo Storico della Fisica e Centro Studi e Ricerche Enrico Fermi</title>
<link href="favicon.ico" rel="shortcut icon" type="image/vnd.microsoft.icon" />
<link rel="stylesheet" type="text/css"
href="https://fonts.googleapis.com/css?family=Ubuntu:regular,bold&subset=Latin">
<link href="e3report.css" rel="stylesheet" type="text/css" />
</head>
<body>  

<div id="page-wrap">
    <p style="margin-bottom:6px;">
    <img src="img/banner_centro_fermi.jpg"
    alt="banner CF" width="800" /></p>

<h2><i>Progetto Extreme Energy Events - La Scienza nelle Scuole</i></h2>
<h1>EEE Report</h1>
<p>&nbsp;</p>

<?php
$school = $_POST["school"];
$msg = trim($_POST["msg"]);
?>
<?php
if ($school == '') {
    echo "<table width=\"600px\"> <tr class=\"red\"><td>";
    echo "<h2>Errore</h2>";
    echo "</td></tr><tr class=\"yellow\"><td style=\"text-align:left;\">";
    echo "Probabilmente non hai scelto il nome del telescopio dalla lista.";
    echo "</td></tr><tr class=\"red\"><td style=\"text-align:left;\">";
    echo "<a href=\"./index.php\">Torna indietro.";
    echo "</td></tr></table>";
    echo "</body></html>";
    exit();
}
?>

<table> <tr class="blue"><td style="border:0px;font-size:24px;">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Messaggio registrato correttamente&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</td></tr><tr class="green"><td style="text-align:left;">
Nome telescopio: <strong><?php echo $school; ?></strong>
</td></tr><tr class="green"><td style="text-align:left; word-wrap: break-word;">
<?php
if ($msg == '') {
    echo "Il messaggio era vuoto, il prossimo report
        non mostrer&agrave; nessun messaggio per il tuo telescopio.";
} else {
    echo"Nel prossimo report automatico verr&agrave; scritto il seguente
        messaggio:<br />"; 
    echo "- ";
    echo $school;
    echo ": ";
    echo $msg; 
    echo "";
}
?>
</td></tr><tr><td>
<p>Se hai sbagliato a inserire il messaggio, puoi inserirlo di nuovo, 
<a href="./index.php">a questo indirizzo</a>.</p>
</td></tr></table>

<?php
$file = './report_messages.txt';
// Open the file to get existing content
$current = file_get_contents($file);
// Append a info
$current .= $school;
$current .= "\t";
$current .= $msg;
$current .= "\n";
// Write the contents back to the file
file_put_contents($file, $current);
?>

</body>
</html>

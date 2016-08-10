<html>
<body>

<?php
$school = $_POST["school"];
$msg = trim($_POST["msg"]);
?>

<?php
if ($school == '') {
    echo "<h2>Errore</h2>";
    echo "<p>Probabilmente non hai scelto il nome della scuola dalla lista.</p>";
    echo "<p><a href=\"./index.php\">Torna indietro.</p>";
    echo "</body></html>";
    exit();
}
?>

<h2>Messaggio registrato</h2>
<p>Nome telescopio: <?php echo $school; ?></p>
<?php
if ($msg == '') {
    echo "<p>Il messaggio era vuoto, il prossimo report
        non mostrer&agrave; nessun messaggio per il tuo telescopio.</p>";
} else {
    echo"<p>Nel prossimo report automatico verr&agrave; scritto il seguente
        messaggio:<br />"; 
    echo "- ";
    echo $school;
    echo ": ";
    echo $msg; 
    echo "</p>";
}
?>
<p>
Se hai sbagliato a inserire il messaggio, puoi inserirlo di nuovo, 
<a href="./index.php">a questo indirizzo</a>.
</p>

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

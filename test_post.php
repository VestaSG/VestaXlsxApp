<?php
// helper for testing VestaXlsxApp

header('Content-Type: text/html; charset=utf-8');

$postData = file_get_contents('php://input');
// var_dump(file_get_contents("php://input"));
// $data = json_decode($postData, true);
echo("<h1>CONTENT_TYPE</h1>" . $_SERVER["CONTENT_TYPE"] . "<br />");
echo("<h1>post data</h1>" . $postData . "<br /><hr /><br />");
echo("<h1>headers</h1>");

foreach (getallheaders() as $name => $value)
{
    echo "$name: $value<br />";
}
echo("<hr /><br />");
// var_dump($data["middle_name"]);
$fnm = $_FILES["file"]["tmp_name"]; // ;"dump.htm";//
$fp = fopen($fnm, "r");
$contents = fread($fp, filesize($fnm));
// echo("<h1>File content</h1>" . $contents . "<br /><hr /><br />");

echo("<h1>POST vars</h1>");

foreach($_POST as $k => $v)
{
	echo($k . ": " . $v . "<br />");
}
?>

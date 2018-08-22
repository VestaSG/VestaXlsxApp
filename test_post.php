<?php
// helper for testing VestaXlsxApp

header('Content-Type: text/html; charset=utf-8');

$postData = file_get_contents('php://input');
// var_dump(file_get_contents("php://input"));
// $data = json_decode($postData, true);
echo($_SERVER["CONTENT_TYPE"] . "<br />" . $postData . "<br />");

// var_dump($data["middle_name"]);

foreach($_POST as $k => $v)
{
	echo($k . ": " . $v . "<br />");
}
?>

<?php
$password = $_GET["P"];
$username = $_GET["u"];
echo($username);
echo($password);


if($username == "admin" && $password == "bob"){
	
	echo("Logged in");
	
}


?>

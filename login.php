<?php
$password = $_GET["psw"];
$username = $_GET["uname"];
echo($username);
echo($password);


if($username == "admin" && $password == "bob"){
	
	echo("Logged in");
	
}


?>

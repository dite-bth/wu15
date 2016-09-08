<?php

session_start();

include ("connect.php");

$_POST["firstname"];
$_POST["lastname"];
$_POST["nickname"];
$_POST["email"];
$_POST["id"];


$query1 = "SELECT * FROM players WHERE firstname = '" .  $_POST["first_name"] . "', lastname = '" .  $_POST["last_name"] . "', nickname = '" .  $_POST["nickname"] . "', id = '" .  $_POST["id"] . "', email = '" .  $_POST["email"] . "' AND score = '" . $_POST["score"] . "'";
//echo $query1;

if ($result = $conn->query($query1))  {  

	if (mysqli_num_rows($result) > 0){
	 		echo "Match!";

		while ($obj = $result->fetch_object()) {

				//Fyller sessionen med värde!
				$_SESSION["nickname"] = $obj->nickname;
				$_SESSION["email"] = $obj->email;



		}   
		header("location:http://localhost/projekt1/views/");   
	 }
	 else {
	 	echo "Wrong username or password!";
	 }
}



?>
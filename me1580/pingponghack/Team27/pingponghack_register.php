<?php
	include("connect.php");

	if(isset($_POST['email']) && $_POST['username']) { //Kollar ifall det finns en post som heter fname och lname.
		//Tillgängliga poster [fname, lname, email, username och password}	
		// Check connection
		if ($conn->connect_error) { //Om anslutningen inte är sönder!
		   die("Connection failed: " . $conn->connect_error); //Post variabler innehåller ingenting. 
		} 
		else {

			$sql = "INSERT INTO  players (firstname, lastname, nickname, id, email, score) VALUES ('" . $_POST['first_name'] . "', '" . $_POST['last_name'] .
                "', '" . $_POST['nickname'] . "', '" . $_POST['id'] . "', '" . $_POST['email'] . "', '" . $_POST['score'] . "')";

			if ($conn->query($sql) === TRUE) {
				echo "Användaren skapad!";
				//echo "<a href='" . "http://link.example.com" . "'>Tryck för att gå tillbaka!</a>";

			} else {
				echo "Kan inte skapa användaren!";
				echo "Error: " . $sql . "<br>" . $conn->error;
				//echo "<a href='" . "http://link.example.com" . "'>Tryck för att försöka igen!</a>";
		     }

		}
	}
	else {
		echo "Email och username not set!";
	}

	$conn->close();

	?>
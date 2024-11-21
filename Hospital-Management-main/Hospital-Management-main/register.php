<?php
$servername = "localhost";  // or your MySQL server address
$username = "root";
$password = "root";
$dbname = "doctor";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Fetch data from POST request
$uid = $_POST['uid'];
$email = $_POST['email'];
$password = $_POST['password'];

// Insert user into database
$sql = "INSERT INTO users (uid, email, password) VALUES ('$uid', '$email', '$password')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>

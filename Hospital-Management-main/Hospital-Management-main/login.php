<?php
$servername = "localhost";  // replace with your server address or IP
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
$email = $_POST['email'];
$password = $_POST['password'];

// Select user from database
$sql = "SELECT * FROM users WHERE email='$email' AND password='$password'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    // Start session
    session_start();
    $_SESSION['user_id'] = $row['id']; // Store user ID in session for future use
    $_SESSION['email'] = $row['email']; // Store user email in session for future use
    // Redirect to dashboard page
    header("Location: dashboard.php");
    exit(); // Ensure script execution stops after redirection
} else {
    echo "Invalid credentials";
}

$conn->close();
?>

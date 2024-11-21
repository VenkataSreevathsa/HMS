<?php
// Start session
session_start();

// Check if user is logged in, if not, redirect to login page
if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}

// Fetch additional patient details from internet resources or any other source
// This part can be customized based on your requirements

// Dummy patient details for demonstration
$patients = array(
    array("name" => "John Doe", "age" => 35, "gender" => "Male", "diagnosis" => "Hypertension"),
    array("name" => "Jane Smith", "age" => 42, "gender" => "Female", "diagnosis" => "Diabetes"),
    array("name" => "Michael Johnson", "age" => 28, "gender" => "Male", "diagnosis" => "Asthma")
);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h2>Welcome to the Dashboard, <?php echo $_SESSION['email']; ?></h2>
        <h3>Patient Consultation Details</h3>
        <table class="table">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Age</th>
                    <th>Gender</th>
                    <th>Diagnosis</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($patients as $patient): ?>
                    <tr>
                        <td><?php echo $patient['name']; ?></td>
                        <td><?php echo $patient['age']; ?></td>
                        <td><?php echo $patient['gender']; ?></td>
                        <td><?php echo $patient['diagnosis']; ?></td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
        <!-- Add additional patient details collection form or any other content here -->
    </div>
</body>
</html>

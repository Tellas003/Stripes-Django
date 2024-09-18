
<?php include "dbconfig.php" ?>
<?php

//session_start();

// Assuming $conn is your database connection object
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Retrieve username and password from the form
$username = $_POST['username'];
$password = $_POST['password'];

// Add necessary security measures like password hashing before comparing
// For demonstration purposes, assuming plain text password in the database
$query = "SELECT * FROM stafflogin WHERE username = '$username' AND password = '$password'";
$query_run = mysqli_query($conn, $query);

if (mysqli_num_rows($query_run) > 0) {
    // Authentication successful
    $_SESSION['username'] = $username;
    $_SESSION['password'] = $password;
    header('Location:index.php '); // Redirect to the dashboard or home page
    exit();
}

else{
    header("Location: stafflogin.php?error=Incorrect Username or Password");
    exit();
}


?>


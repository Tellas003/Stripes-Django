<?php
include 'dbconfig.php'; // Include your database connection file

// Function to get visitor IP address
function get_ip_address() {
    // Check for shared internet/ISP IP
    if (!empty($_SERVER['HTTP_CLIENT_IP']) && filter_var($_SERVER['HTTP_CLIENT_IP'], FILTER_VALIDATE_IP)) {
        return $_SERVER['HTTP_CLIENT_IP'];
    }
    // Check for IP behind a proxy
    elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR']) && filter_var($_SERVER['HTTP_X_FORWARDED_FOR'], FILTER_VALIDATE_IP)) {
        return $_SERVER['HTTP_X_FORWARDED_FOR'];
    }
    // Check for public IP address
    else {
        return $_SERVER['REMOTE_ADDR'];
    }
}

// Store visitor data in the database
$ip_address = get_ip_address();
$date = date('Y-m-d');

// Check if the visitor's IP address already exists for today's date
$query = "SELECT * FROM website_visitors WHERE ip_address = '$ip_address' AND date = '$date'";
$result = mysqli_query($conn, $query);
if (mysqli_num_rows($result) == 0) {
    // If the IP address doesn't exist for today, insert a new record
    $insert_query = "INSERT INTO website_visitors (ip_address, date) VALUES ('$ip_address', '$date')";
    mysqli_query($conn, $insert_query);
}

mysqli_close($conn);
?>

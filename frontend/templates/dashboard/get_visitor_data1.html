<?php
include 'dbconfig.php'; // Include your database connection file

// Fetch visitor data date-wise
$query = "SELECT date, COUNT(*) AS visitor_count, GROUP_CONCAT(ip_address) AS ip_address FROM website_visitors GROUP BY date";
$result = mysqli_query($conn, $query);

// Store data in an associative array
$data = array();
while ($row = mysqli_fetch_assoc($result)) {
    $data[$row['date']] =  $row['visitor_count'];
       $data[$row['ip_address']] = $row['ip_address'];
    
}

// Convert data to JSON format and output
echo json_encode($data);
?>

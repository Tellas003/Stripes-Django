
<?php
include('includes/header.php'); 
include('includes/navbar1.php'); 
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
    <title>Registration Form</title>
</head>
<body>

<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <h2 class="text-center mb-4"> Student Registration</h2>
            <form action="#" method="post">
                <div class="form-group">
                    <label for="courseName">Course Name:</label>
                    <input type="text" class="form-control" id="courseName" name="courseName" required>
                </div>
                <div class="form-group">
                    <label for="certificateNo">Certificate No:</label>
                    <div style="display: flex; align-items: center;">
        <span id="certificateStripes" name="certificateStripes"style="padding: 8px; border: 1px solid #ccc; border-radius: 4px; background-color: #eee;">Stripes/</span>
        <select id="certificateCourse" name="certificateCourse" required style="padding: 8px; border: 1px solid #ccc; border-radius: 4px; background-color: #eee;">
        <option value="Stripes">Select Course</option>
        <option value="BTRM">BTRM/</option>
        <option value="PCCW">PCCW/</option>
         <option value="SSBT">SSBT/</option>
          <option value="ES">ES/</option>
           <option value="SCALE">SCALE/</option>
            <option value="VERC">VERC/</option>
             <option value="EEAC">EEAC/</option>
              <option value="FRAMO">FRAMO/</option>
               <option value="BWTS-NK">BWTS-NK/</option>
                <option value="ME">ME/</option>
                 <option value="BWTS-SP">BWTS-SP/</option>
                  <option value="INST">INST/</option>
                   <option value="VECME">VECME/</option>
                     <option value="SSSHT">SSSHT/</option>
      </select>
                    <input type="text" class="form-control" id="certificateNo" name="certificateNo" required>
                </div></div>
                <div class="form-group">
                    <label for="participantName">Student First Name:</label>
                    <input type="text" class="form-control" id="participantName" name="participantName" required>
                </div>
                <div class="form-group">
                    <label for="participantName">Student Last Name:</label>
                    <input type="text" class="form-control" id="lastName" name="lastName" required>
                </div>
                <div class="form-group">
                    <label for="passportNumber">Seminar Book/Passport Number:</label>
                    <input type="text" class="form-control" id="passportNo" name="passportNo" required>
                </div>
                <div class="form-group">
                    <label for="startDate">Course Start Date:</label>
                    <input type="date" class="form-control" id="courseDate1" name="courseDate1" required>
                </div>
                <div class="form-group">
                    <label for="endDate">Course End Date:</label>
                    <input type="date" class="form-control" id="courseDate2" name="courseDate2" required>
                </div>
                <div class="form-group">
                    <label for="certificateIssue">Certificate Issue Date:</label>
                    <input type="date" class="form-control" id="issueDate" name="issueDate" required>
                </div>
                <button type="submit" class="btn btn-primary btn-block">Submit</button>
            </form>
        </div>
    </div>
</div>

</body>
</html>

<?php include "dbconfig.php" ?>
<?php

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Process form data
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $courseName = $_POST["courseName"];
    $certificateStripes = "Stripes/";
    $certificateCourse = $_POST["certificateCourse"];
    $certificateNo = $_POST["certificateNo"];
    $participantName = $_POST["participantName"];
    $lastName=$_POST["lastName"];
    $passportNo = $_POST["passportNo"];
    $courseDate1 = $_POST["courseDate1"];
    $courseDate2 = $_POST["courseDate2"];
    $issueDate = $_POST["issueDate"];

    // Check if certificate number already exists in the database
   // $checkExistingQuery = "SELECT * FROM verification WHERE certificateNo = '$certificateNo'";
    $checkExistingQuery = "SELECT * FROM verification_1 WHERE certificateStripes = '$certificateStripes' AND certificateCourse = '$certificateCourse/' AND certificateNo = '$certificateNo'";

    $result = $conn->query($checkExistingQuery);

    if ($result->num_rows > 0) {
        ?>
        <script>
        swal({
            title: "Error!",
            text: "Data with this Certificate No already exists in the database. Please enter a different Certificate No.",
            icon: "error",
        });
        </script>
        <?php
        exit();
    }

    // Insert data into the database
    $insertQuery = "INSERT INTO verification_1 (courseName,certificateStripes,certificateCourse,certificateNo, participantName, lastName, passportNo, courseDate1, courseDate2, issueDate)
                    VALUES ('$courseName', '$certificateStripes','$certificateCourse/','$certificateNo', '$participantName', '$lastName', '$passportNo', '$courseDate1', '$courseDate2', '$issueDate')";

    if ($conn->query($insertQuery) === TRUE) {
        ?>
        <script>
        swal({
            title: "Success!",
            text: "Your Data Inserted!",
            icon: "success",
        });
        </script>
        <?php
        exit();
    } else {
        echo "Error: " . $insertQuery . "<br>" . $conn->error;
    }
}

$conn->close();
?>

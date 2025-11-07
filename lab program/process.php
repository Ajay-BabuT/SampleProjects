<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Data Output</title>
</head>
<body>
    <h2>Submitted Fotm Data</h2>
    <?php
    if($_SERVER["REQUEST_METHOD"]=="POST"){
        $name=$_POST['name'];
        $email=$_POST['email'];
        $age=$_POST['age'];
        
        echo "Name : ".htmlspecialchars($name)."<br>";
        echo "Email : ".htmlspecialchars($email)."<br>";
        echo "Age : ".htmlspecialchars($age)."<br>";
    }else{
        echo "Please submit the form first";
    }
    ?>
</body>
</html>
<?php
ini_set('upload_max_filesize','10M');
//echo ini_get('upload_max_filesize'),",",ini_get('post_max_size');
//die();
//var_dump($_FILES);
//var_dump($_POST);die();
$target_dir = "uploads/";
$destination ="uploads/mitsos.png";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);
// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    if($check !== false) {
        echo "File is an image - " . $check["mime"] . ".";
        $uploadOk = 1;
	if(move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $destination)) {echo "<img src=$destination>"; }
    } else {
        echo "File is not an image.";
        $uploadOk = 0;
    }
}
?>

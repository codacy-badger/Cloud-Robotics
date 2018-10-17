
<?php 

	$file_path = "recording/";

	$file_path = $file_path . basename($_FILES['uploaded_file']['name']);

	if(move_uploaded_file($_FILES['uploaded_file']['tmp_name'],$file_path))	{
		echo "success";
		$myfile = fopen("/zstorage/home/ictest00577/public_html/status.txt", "w") or die("Unable to open file!");
		fwrite($myfile, 22);
		fclose($myfile);
	}else {
		echo "error";
	}


 ?>

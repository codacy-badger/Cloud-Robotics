<?php

	$file = "start.txt";
	$handle = fopen($file , "r");
	$contents = fread($handle, filesize($file ));
	fclose($handle);
	fclose($file);

	if ($contents == 1) {
		$file = fopen("start.txt","w");
		echo fwrite($file,"0");
		fclose($file);;
	}
	if ($contents == 0) {
		$file = fopen("start.txt","w");
		echo fwrite($file,"1");
		fclose($file);;
	}




?>
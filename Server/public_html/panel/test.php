<?php
$myfile = fopen("moves.txt", "r");
$str = fread($myfile,filesize("moves.txt"));
fclose($myfile);

// negative limit (since PHP 5.1)
print_r(explode(' +', $str));
?>
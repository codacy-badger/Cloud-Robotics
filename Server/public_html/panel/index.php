<?php
$page = $_SERVER['PHP_SELF'];
$sec = "5";
?>

<!DOCTYPE html>
<html lang="en" >

<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="<?php echo $sec?>;URL='<?php echo $page?>'">

  <title>Control interface</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js" type="text/javascript"></script>

  <link href='https://fonts.googleapis.com/css?family=Varela+Round' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Monoton' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

  <link rel='stylesheet prefetch' href='https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css'>

      <link rel="stylesheet" href="css/style.css">

<script>
 
function imAnAjaxFunction(){
 
  	var request = $.ajax({
   		url: 'ajax.php',
   		type: 'get',
   		dataType: 'html'
 	});
 
	request.done( function ( data ) {
 		$('#ajaxButton').html( data );
 	});
 
	request.fail( function ( jqXHR, textStatus) {
 		console.log( 'Sorry: ' + textStatus );
 	});
 
}
 
</script>

</head>

<body>

<?php

	$file = "start.txt";
	$handle = fopen($file , "r");
	$contents = fread($handle, filesize($file ));
	fclose($handle);
	fclose($file);
	$r = (1 == $contents ) ? 'Working' : 'Not Working';

	$file = "person.txt";
	$handle = fopen($file , "r");
	$contents = fread($handle, filesize($file ));
	fclose($handle);
	fclose($file);

	if (0 == $contents)
  		$d = 'We have not found someone';
	if (1 == $contents)
  		$d = 'Someone needs Help!';
	if (2 == $contents)
  		$d = 'We have found someone';




	$myfile = fopen("moves.txt", "r");
	$f = fread($myfile,filesize("moves.txt"));
	fclose($myfile);





?>

  <div id="particles-js">
  <div class="container">
    <div class="row top">
      <div class="twelve column">

        <h1>Control Panel</h1>
        <h2> Cloud Brained Informations</h2>
      </div>
    </div>
    
    <div class="row">
      <div class="one-half column">
        <div class="pens pulled">
          <h1>Informations</h1>
    <a>      
The robot now is: 

<?=$r?><br />
<?=$d?><br />

The robot has already done the following moves: 
<br />
<?=$f?><br />
<br />
<img src="/image_upload/uploads/image.jpg" alt="icon" height="250" width="420"/>
 </a>
        </div>
      </div>

      <div class="one-half column">
        <div class="posts pulled">
          <h1>Start Button</h1>
     <a class="button btn-sm" name="insert"  id = 'ajaxButton' href="" onClick = 'imAnAjaxFunction()' >    <span class="glyphicon glyphicon-off"></span>    </a>
 
        </div>
      </div>
    </div>
  </div>

<div class="container ">
  <div class="footer">
  <p>By Georgios Angelopoulos </p> </div></div>
  </div>
  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/particles.js/2.0.0/particles.min.js'></script>

  

    <script  src="js/index.js"></script>




</body>

</html>

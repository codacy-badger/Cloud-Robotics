<?php

$error = "";

$success = "";

  if(isset($_POST['submit'])){

    $uname = $_POST['uname'];

    $pass = $_POST['pass'];

    if($uname == "admin"){

      if($pass == "hyperion"){

        $error = "";

        $success = "Welcome ".$uname." !!!";
	//redirect to the welcome.php page

	header("Location: http://83.212.106.184/panel/");
	die();
      }

      else {

        $error = "Invalid Password !!!";

        $success = "";

      }

    }

    else {

      $error = "Invalid Username !!!";

      $success = "";

    }

  }


 ?>





<!DOCTYPE html>
<html lang="en" >

<head>

  <title>Login</title>
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700" rel="stylesheet">
    <meta charset="UTF-8">



  <script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js" type="text/javascript"></script>

  <link href='https://fonts.googleapis.com/css?family=Varela+Round' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Monoton' rel='stylesheet' type='text/css'>
  
<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">

      <link rel="stylesheet" href="css/style.css">

  <style>
body {
  background-color: #2c3338;
  color: #606468;
  font-family: 'Open Sans', sans-serif;
  font-size: 14px;
  font-size: 0.875rem;
  font-weight: 400;
  height: 100%;
  line-height: 1.5;
  margin: 0;
  min-height: 100vh;
}
</style>

  
</head>


  <body class="align">
<br>

  <div class="grid">

    <form method="post" class="form login">

      <div class="form__field">
        <label for="login__username"><span class="hidden">Username</span><i class="material-icons">supervisor_account</i>
</label>
        <input id="login__username" type="text" name="uname" class="form__input" placeholder="Username" required>
      </div>

      <div class="form__field">
        <label for="login__password"><span class="hidden">Password</span><i class="material-icons">fingerprint</i></label>
        <input id="login__password" type="password" name="pass" class="form__input" placeholder="Password" required>
      </div>

      <div class="form__field">
        <input type="submit" name="submit" value="Log In">
      </div>

    </form>

      <p class="red"><?php echo $error; ?></p>

      <p class="green"><?php echo $success; ?></p>
  </div>



<br>
  <p>By Georgios Angelopoulos </p> </div></div></div>
  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/particles.js/2.0.0/particles.min.js'></script>

  

    <script  src="js/index.js"></script>
  

</body>

</html>

<?php
include 'includes/api.php';
include 'includes/render.php';


if(!isset($_POST['user_name']) or !isset($_POST['user_password']) or !isset($_POST['user_fullname'])) {
    echo render('register.html.twig', array());
    die();
}

$ret =  CallAPI("POST", "register", ["user_name" => $_POST['user_name'], "user_fullname" => $_POST['user_fullname'],  "user_password" => $_POST['user_password']]);

if ($ret == False){
    echo render('login.html.twig',  array("error" => "Le nom d'utilisateur existe déjà!"));
    die();
}

else {
    echo render('register_ok.html.twig', array());
    die();
}

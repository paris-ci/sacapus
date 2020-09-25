<?php

include 'includes/api.php';
include 'includes/render.php';

if(!isset($_POST['user_name']) or !isset($_POST['user_password'])) {
    echo render('login.html.twig', array("error" => "Tous les champs sont requis!"));
    die();
}

$_SESSION['token'] = CallAPI("POST", "login", ["user_name" => $_POST['user_name'], "user_password" => $_POST['user_password']]);
$_SESSION['user_name'] = $_POST['user_name'];


if ($_SESSION['token'] == False){
    echo render('login.html.twig', array("error" => "Utilisateur ou mot de passe faux :("));
    die();
}
elseif (!isset($_SESSION['token'])) {
    echo render('login.html.twig', array("error" => "Erreur lors de la connexion"));
    die();
}
else {
    header('Location: /user.php');
    die();
}

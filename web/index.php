<?php
include 'includes/api.php';
include 'includes/render.php';

header('Location: /login.php');
die();
echo render('index.html.twig', array());

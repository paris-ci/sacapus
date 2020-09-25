<?php
/**
 * Created by IntelliJ IDEA.
 * User: arthur
 * Date: 14/05/2018
 * Time: 18:25
 */

//include 'includes/api.php';
include 'includes/protection.php';
include 'includes/render.php';




if(!isset($_POST['location_name'])) {
    echo render('learn_form.html.twig', array());
    die();
}

CallAPI("POST", "create_task", ["type"=>"learn", "arguments"=>$_POST['location_name']]);
echo render('learning.html.twig', array(
    "user" => CallAPI("GET", "user_info"),
    "duration" => 1000000,
    "location" => $_POST['location_name']
));



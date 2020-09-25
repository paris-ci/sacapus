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

$positions = CallAPI("GET", "get_positions");
echo render('user.html.twig', array(
    "user" => CallAPI("GET", "user_info"),
    "positions" => $positions,
    "last_located" => end($positions),
    ));



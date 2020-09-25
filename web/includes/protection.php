<?php
/**
 * Created by IntelliJ IDEA.
 * User: arthur
 * Date: 14/05/2018
 * Time: 17:51
 */


include 'api.php';
if (!isset($_SESSION['user_name']) or !isset($_SESSION['token'])){
    header('Location: /login.php');
    die();
}

$ui = CallAPI("GET", "user_info");
if (!isset($ui->fullname)){
    header('Location: /login.php');
    die();
}
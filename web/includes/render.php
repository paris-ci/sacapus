<?php
/** @noinspection PhpUnhandledExceptionInspection */
/**
 * Created by IntelliJ IDEA.
 * User: arthur
 * Date: 14/05/2018
 * Time: 18:13
 */

require_once __DIR__ . '/../vendor/autoload.php';

function render($file, $params)
{
    $loader = new Twig_Loader_Filesystem(__DIR__ .'/../templates');
    $twig = new Twig_Environment($loader, array(
        //'cache' => 'templates/compilation_cache',
    ));
    return $twig->render($file, $params);
}
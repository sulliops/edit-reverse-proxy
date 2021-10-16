<?php
  ini_set('display_errors', 1);
  ini_set('display_startup_errors', 1);
  error_reporting(E_ALL);

  echo "Starting...";
  
  $listenOn = $_GET["listenOn"];
  echo $listenOn;
  $toProxy = $_GET["toProxy"];
  echo $toProxy;
  shell_exec('python3 /var/edit-reverse-proxy/edit-reverse-proxy.py ' '.$listenOn.' '.$toProxy.');
?>
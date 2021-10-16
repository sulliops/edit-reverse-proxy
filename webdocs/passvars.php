<?php
  $listenOn = $_GET["listenOn"];
  echo $listenOn;
  $toProxy = $_GET["toProxy"];
  echo $toProxy;
  $listenOn=escapeshellarg($listenOn);
  $toProxy=escapeshellarg($toProxy);
  exec('python3 /var/edit-reverse-proxy/edit-reverse-proxy.py ".$listenOn." ".$toProxy."');
?>
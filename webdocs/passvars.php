<?php
  $listenOn = $_GET["listenOn"];
  echo $listenOn;
  $toProxy = $_GET["toProxy"];
  echo $toProxy;
  $listenOn=escapeshellarg($listenOn);
  $toProxy=escapeshellarg($toProxy);
  shell_exec("python3 /var/edit-reverse-proxy/edit-reverse-proxy.py 1 8080");
?>
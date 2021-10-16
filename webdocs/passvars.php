<?php
  $listenOn = $_GET["listenOn"];
  echo $listenOn;
  $toProxy = $_GET["toProxy"];
  echo $toProxy;
  shell_exec('python3 /var/edit-reverse-proxy/edit-reverse-proxy.py "'.$listenOn.'" "'.$toProxy.'"');
?>
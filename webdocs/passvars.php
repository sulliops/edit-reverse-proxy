<?php
  $listenOn = $_GET["listenOn"]; // Get listenOn variable from URL (passed with JavaScript from index.html)
  
  $toProxy = $_GET["toProxy"]; // Get toProxy variable from URL (passed with JavaScript from index.html)
  
  $listenOn = escapeshellarg($listenOn); // Escape any special characters in listenOn
  $toProxy = escapeshellarg($toProxy); // Escape any special characters in toProxy
  
  echo file_get_contents('success.html'); // Echo contents of success.html
  $pass_vars = exec('sudo python3 /var/edit-reverse-proxy/edit-reverse-proxy.py "'.$listenOn.'" "'.$toProxy.'"'); // Execute edit-reverse-proxy.py with arguments listenOn and toProxy
?>

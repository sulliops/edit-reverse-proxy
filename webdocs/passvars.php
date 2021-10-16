<?php
    $listenOn = $_GET["listenOn"];
    $toProxy = $_GET["toProxy"];
    shell_exec('python3 /var/edit-reverse-proxy/edit-reverse-proxy.py '.$listenOn.' '.$toProxy.');
?>
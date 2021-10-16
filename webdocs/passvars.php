<?php
  $listenOn = $_GET["listenOn"]; // Get listenOn variable from URL (passed with JavaScript from index.html)
  
  $toProxy = $_GET["toProxy"]; // Get toProxy variable from URL (passed with JavaScript from index.html)
  
  $listenOn = escapeshellarg($listenOn); // Escape any special characters in listenOn
  $toProxy = escapeshellarg($toProxy); // Escape any special characters in toProxy
  
  $result = exec('python3 /var/edit-reverse-proxy/edit-reverse-proxy.py "'.$listenOn.'" "'.$toProxy.'"'); // Execute edit-reverse-proxy.py with arguments listenOn and toProxy
  
  if ($result == "Success!") {
    echo("
<!DOCTYPE html>
<html lang='en'>
   <head>
      <meta charset='utf-8' />
      <meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no' />
      <meta name='description' content='' />
      <meta name='author' content='' />
      <title>edit-reverse-proxy | Reverse Proxy Editor</title>
      <link rel='icon' type='image/x-icon' href='assets/favicon.ico' />
      <link href='css/styles.css' rel='stylesheet' />
   </head>
   <body>
      <div class='d-flex' id='wrapper'>
         <div class='border-end bg-white' id='sidebar-wrapper'>
            <div class='sidebar-heading border-bottom bg-light'>edit-reverse-proxy</div>
            <div class='list-group list-group-flush'><a class='list-group-item list-group-item-action list-group-item-light p-3' href='#!'>Dashboard</a></div>
         </div>
         <div id='page-content-wrapper'>
            <nav class='navbar navbar-expand-lg navbar-light bg-light border-bottom'>
               <div class='container-fluid'><button class='btn btn-primary' id='sidebarToggle'>Toggle Menu</button></div>
            </nav>
            <div class='container-fluid'>
               <h1 class='mt-4'>edit-reverse-proxy | Reverse Proxy Editor</h1>
               <p>A combination of PHP and Python script that makes configuring and editing a single reverse proxy easy.</p>
               <p>This script assumes NGINX was never configured on the server prior to running <code>configure-nginx.py</code>. Issues may arise on servers where Apache2 or an existing NGINX installation are present.</p>
               <br>
               <h2 class='mt-4'>Edit configuration:</h2>
               <h4 class='mt-4'>Port number for reverse proxy (default 80):</h4>
               <p>The port on which the reverse proxy will be exposed. Example: if you're attempting to proxy a service on port <code>2100</code>, and you want to make it available on your domain at <code>http://domain.com</code>, you would serve at port <code>80</code>. If a port is not specified, the default of <code>80</code> will be used.</p>
               <input class='form-control' type='number' id='listenOn' minlength='1' maxlength='65535' placeholder='Enter a port number or leave blank for 80...' />
               <h4 class='mt-4'>Port to be proxied:</h4>
               <p>The port on which the service you want to proxy is running.</p>
               <input class='form-control' type='number' id='toProxy' required minlength='1' maxlength='65535' placeholder='Enter a port number...' /><br><button class='btn btn-primary' onclick='sendVarsToPHP();'>Submit</button>
            </div>
         </div>
      </div>
      <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js'></script><script src='js/scripts.js'></script>
   </body>
</html>
    ")
  }
?>
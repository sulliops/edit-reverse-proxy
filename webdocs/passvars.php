<?php
  $listenOn = $_GET["listenOn"]; // Get listenOn variable from URL (passed with JavaScript from index.html)
  
  $toProxy = $_GET["toProxy"]; // Get toProxy variable from URL (passed with JavaScript from index.html)
  
  $listenOn = escapeshellarg($listenOn); // Escape any special characters in listenOn
  $toProxy = escapeshellarg($toProxy); // Escape any special characters in toProxy
  
  $result = exec('sudo python3 /var/edit-reverse-proxy/edit-reverse-proxy.py "'.$listenOn.'" "'.$toProxy.'"'); // Execute edit-reverse-proxy.py with arguments listenOn and toProxy
  $result = "Success!";
  echo $result;
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>edit-reverse-proxy | Reverse Proxy Editor</title>
        <!-- Favicon-->
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
        <!-- Core theme CSS (includes Bootstrap)-->
        <link href="css/styles.css" rel="stylesheet" />
    </head>
    <body>
        <div class="d-flex" id="wrapper">
            <!-- Sidebar-->
            <div class="border-end bg-white" id="sidebar-wrapper">
                <div class="sidebar-heading border-bottom bg-light">edit-reverse-proxy</div>
                <div class="list-group list-group-flush">
                    <a class="list-group-item list-group-item-action list-group-item-light p-3" href="#!">Dashboard</a>
                </div>
            </div>
            <!-- Page content wrapper-->
            <div id="page-content-wrapper">
                <!-- Top navigation-->
                <nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
                    <div class="container-fluid">
                        <button class="btn btn-primary" id="sidebarToggle">Toggle Menu</button>
                    </div>
                </nav>
                <!-- Page content-->
                <div class="container-fluid">
                    <h1 class="mt-4">Success!</h1>
                    <p>The changes to your reverse proxy configuration have been made successfully.</p>
                    <br>
                    <button class="btn btn-primary" onclick="goBack();">Back to home page</button>
                </div>
            </div>
        </div>
        <!-- Bootstrap core JS-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js"></script>
        <!-- Core theme JS-->
        <script src="js/scripts.js"></script>
        <!-- Custom JS -->
        <script>
            function goBack() { // Go back to home page
                window.location.href = "index.html"; // Set URL to index.html
            }
        </script>
    </body>
</html>
# edit-reverse-proxy

edit-reverse-proxy is a combination of scripts meant to make creating a single NGINX reverse proxy easier.

Where normally a user would edit NGINX configuration files through the command-line interface, these scripts automate the process and allow users to enter port numbers for the port being exposed and the port being proxied through a simple web-based interface.

This repository was developed as part of [CUHackIt Hello World 2021](https://cuhack.it/#/) over the course of eight hours.

Below is a list of each major file and its function:

### makefile

The makefile runs Linux commands which copy the contents of `webdocs` and the `edit-reverse-proxy.py` script into absolute locations for use and editing, and it sets permissions for individual files so that NGINX and Python can access/modify them.

### configure-nginx.py

This script installs NGINX and PHP-FPM, and sets NGINX's default configuration files to enable the execution of PHP scripts on the web server. 

Additionally, this script creates the `edit-reverse-proxy.conf` file which stores the configuration for the reverse proxy.

### index.html

The `index.html` file (and its associated CSS/JS/favicon) are the front-end for this script that allows users to simply input the appropriate port numbers in an easy-to-understand interface.

There is an associated function, `sendVarsToPHP()`, which redirects the browser to `passvars.php` with user-inputted parameters.

### passvars.php

`passvars.php` interprets URL paramaters as variables, then passes the variables (user input) to `edit-reverse-proxy.py` as arguments for interpretation.

A front-end "success" page is also displayed.

### edit-reverse-proxy.py

This script gets the current contents of `edit-reverse-proxy.conf`, converts the contents to a line-by-line array, then modifies the contents of certain lines to match user input. The script then writes the array line-by-line back to `edit-reverse-proxy.conf`.

# Usage

`python3` must be installed:

```
apt-get install python3
```

Clone the repository to a local folder and `cd`:

```
git clone https://github.com/sulliops/edit-reverse-proxy.git
cd edit-reverse-proxy/
```

Run the makefile:

```
make build
```

Visit the newly-created web server at `http://localhost:80` and begin interacting with the scripts.

# Important note

This script will destroy any changes made to the `default` NGINX configuration.

In addition, this script will not allow proxying over the same port that the script runs on (default 8080). Editing `configure-nginx.py` to run the script on a port other than default will free up that port, assuming no other program tries to bind to it.

# Contributors

**Julianne Johnsonwall** [(@jjohn67)](https://github.com/jjohn67) — Python, JavaScript, HTML

**Alexis Knezek** [(@Alexiswka)](https://github.com/Alexiswka) — Python, HTML

**Kate Knezek** [(@Katewka)](https://github.com/Katewka) — Python, HTML

**Owen Sullivan** [(@sulliops)](https://github.com/sulliops) — Python, JavaScript, HTML, PHP

# References

Some input was given by various members of the CUHackIt mentor team, which enabled debugging and completion of various parts of this project ranging from the makefile to PHP.

Input also came from sources such as StackOverflow and other online resources.

The template for the front-end of the script was provided by [Start Bootstrap](https://startbootstrap.com/template/simple-sidebar).
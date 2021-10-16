from subprocess import run, CalledProcessError
import os
import shutil

try:
    run(['apt-get', 'update'], capture_output=True).stdout
except CalledProcessError as e:
    print(e.output)

try:
    run(['apt-get', 'install', '-y', 'nginx'], capture_output=True).stdout
except CalledProcessError as e:
    print(e.output)

with open('/etc/nginx/sites-enabled/edit-reverse-proxy.conf', 'w') as proxy_conf_file:
    initial_config = ['server {\n', 'listen 80;\n', 'listen [::]:80;\n', '\n', 'access_log /var/log/nginx/reverse-access.log;\n', 'error_log /var/log/nginx/reverse-error.log;\n', '\n', 'location / {\n', 'proxy_pass http://127.0.0.1:8000;\n', '}\n', '}\n']
    proxy_conf_file.writelines(initial_config)

proxy_conf_file.close()

try:
    run(['apt-get', 'install', '-y', 'php-fpm'], capture_output=True).stdout
except CalledProcessError as e:
    print(e.output)

# with open('/etc/nginx/nginx.conf') as nginx_conf_file:
#     php_enabled = ['']
#     nginx_conf_file.writelines(php_enabled)

# nginx_conf_file.close()

with open('/etc/nginx/sites-enabled/default') as default_conf_file:
    fastcgi_enabled = ['server {\n', 'listen 80 default_server;\n', 'listen [::]:80 default_server;\n', '\n', 'root /var/www/html;\n', '\n', 'index index.html index.htm index.nginx-debian.html;\n', '\n', 'server_name _;\n', '\n', 'location / {\n', 'try_files $uri $uri/ =404;\n', '}\n', '\n', 'location ~ \.php$ {\n', 'include snippets/fastcgi-php.conf;\n', '\n', 'fastcgi_pass unix:/run/php/php7.3-fpm.sock;\n', 'include fastcgi_params;\n', '}\n', '}\n']
    default_conf_file.writelines(fastcgi_enabled)

default_conf_file.close()
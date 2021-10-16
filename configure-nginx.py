from subprocess import run, CalledProcessError
import os
import shutil

# Run apt-get update
try:
    run(['apt-get', 'update'], capture_output=True).stdout
except CalledProcessError as e:
    print(e.output)

# Install nginx package
try:
    run(['apt-get', 'install', '-y', 'nginx'], capture_output=True).stdout
except CalledProcessError as e:
    print(e.output)

# Create new nginx config file for reverse proxy
with open('/etc/nginx/sites-enabled/edit-reverse-proxy.conf', 'w') as proxy_conf_file:
    initial_config = ['server {\n', 'listen 80;\n', 'listen [::]:80;\n', '\n', 'access_log /var/log/nginx/reverse-access.log;\n', 'error_log /var/log/nginx/reverse-error.log;\n', '\n', 'location / {\n', 'proxy_pass http://127.0.0.1:8000;\n', '}\n', '}\n']
    proxy_conf_file.writelines(initial_config)
# Close file
proxy_conf_file.close()

# Install php-fpm
try:
    run(['apt-get', 'install', '-y', 'php-fpm'], capture_output=True).stdout
except CalledProcessError as e:
    print(e.output)

# Modify base nginx config file with lines enabling php
with open('/etc/nginx/nginx.conf', 'w') as nginx_conf_file:
    php_enabled = ['user www-data;\n', 'worker_processes auto;\n', 'pid /run/nginx.pid;\n', 'include /etc/nginx/modules-enabled/*.conf;\n', '\n', 'events {\n', 'worker_connections 768;\n','}\n', '\n', 'http {\n', '\n', 'sendfile on;\n', 'tcp_nopush on;\n', 'tcp_nodelay on;\n','keepalive_timeout 65;\n', 'types_hash_max_size 2048;\n', 'server_tokens off;\n', '\n','include /etc/nginx/mime.types;\n', 'default_type application/octet-stream;\n','\n','ssl_protocols TLSv1 TLSv1.1 TLSv1.2;\n', 'ssl_prefer_server_ciphers on;\n', '\n','access_log /var/log/nginx/access.log;\n', 'error_log /var/log/nginx/error/log;\n', '\n','gzip on;\n', '\n', 'include /etc/nginx/conf.d/*.conf;\n', 'include /etc/nginx/sites-enabled/*;\n']
    nginx_conf_file.writelines(php_enabled)
# Close file
nginx_conf_file.close()

# Modify default nginx config file with lines enabling php
with open('/etc/nginx/sites-enabled/default', 'w') as default_conf_file:
    fastcgi_enabled = ['server {\n', 'listen 80 default_server;\n', 'listen [::]:80 default_server;\n', '\n', 'root /var/www/html;\n', '\n', 'index index.html index.htm index.nginx-debian.html;\n', '\n', 'server_name _;\n', '\n', 'location / {\n', 'try_files $uri $uri/ =404;\n', '}\n', '\n', 'location ~ \.php$ {\n', 'include snippets/fastcgi-php.conf;\n', '\n', 'fastcgi_pass unix:/run/php/php7.3-fpm.sock;\n', 'include fastcgi_params;\n', '}\n', '}\n']
    default_conf_file.writelines(fastcgi_enabled)
# Close file
default_conf_file.close()
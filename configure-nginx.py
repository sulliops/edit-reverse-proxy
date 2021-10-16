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

#with open('/etc/nginx/nginx.conf') as nginx_conf_file:
#    php_enabled = ['']
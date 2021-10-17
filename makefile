build:
	apt-get install nginx
	rm -rf /var/www/html/
	mkdir /var/www/html/
	cp -r webdocs/* /var/www/html/
	rm -rf /var/edit-reverse-proxy/
	mkdir /var/edit-reverse-proxy/
	cp edit-reverse-proxy.py /var/edit-reverse-proxy/edit-reverse-proxy.py
	chmod 777 /etc/nginx/sites-enabled/default
	chmod 777 /etc/nginx/nginx.conf
	python3 configure-nginx.py
	chmod 777 /etc/nginx/sites-enabled/edit-reverse-proxy.conf
	chown -R www-data:www-data /var/log/nginx
	chmod -R 755 /var/log/nginx
	rm -rf /var/log/nginx/error/
	mkdir /var/log/nginx/error/
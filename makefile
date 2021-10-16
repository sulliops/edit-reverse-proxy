build:
	rm -rf /var/www/html/
	mkdir /var/www/html/
	cp -r webdocs/* /var/www/html/
	rm -rf /var/edit-reverse-proxy/
	mkdir /var/edit-reverse-proxy/
	mv edit-reverse-proxy.py /var/edit-reverse-proxy/edit-reverse-proxy.py
	python3 configure-nginx.py
	chmod 777 /etc/nginx/sites-enabled/edit-reverse-proxy.conf
build:
	rm -rf /var/www/html/
	mkdir /var/www/html/
	mv webdocs/* /var/www/html/
	mkdir /var/edit-reverse-proxy/
	mv edit-reverse-proxy.py /var/edit-reverse-proxy/edit-reverse-proxy.py
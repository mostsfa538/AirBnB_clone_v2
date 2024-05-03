#!/usr/bin/env bash
# Prepare your web servers

sudo apt update
sudo apt install -y nginx

sudo service nginx start
sudo ufw allow " Nginx HTTP"

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.htm

printf %s "<html>
  <head>
  </head>
  <body>
    <h4>Holberton School</h4>
  </body>
</html>" | sudo tee file /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/server_name _;/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart

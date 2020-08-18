#!/usr/bin/env bash
# Prepare web servers 
sudo apt-get update
sudo apt -y install nginx
sudo mkdir -p /data/web_static/shared /data/web_static/releases/test
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
LINE_TO_REPL="server_name _;"
REPLACE_FOR="server_name _;\n\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "s:$LINE_TO_REPL:$REPLACE_FOR:" /etc/nginx/sites-available/default
sudo service nginx restart

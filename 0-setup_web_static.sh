#!/usr/bin/env bash
# Prepare web servers 
sudo apt-get update
sudo apt -y install nginx
sudo mkdir -p /data/web_static/shared /data/web_static/releases/test
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
LINE_TO_REPL="# pass the PHP scripts to FastCGI server listening on 127.0.0.1\:9000"
REPLACE_FOR="\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\n# pass the PHP scripts to FastCGI server listening on 127.0.0.1\:9000"
sudo sed -i "s:$LINE_TO_REPL:$REPLACE_FOR:" /etc/nginx/sites-enabled/default
sudo service nginx restart


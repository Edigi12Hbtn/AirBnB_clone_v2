#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from
 the contents of the web_static folder.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """create a compressed file from web_static directory."""
    local("mkdir -p versions", capture=True)
    time = datetime.now()
    date = time.strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(date)
    if local("tar -czvf {} web_static/".format(path), capture=False):
        return path
    else:
        return None

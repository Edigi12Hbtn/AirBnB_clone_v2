#!/usr/bin/python3
"""
Fabric script that distributes an archive to your
 web servers, using the function do_deploy.
"""
from fabric.api import local, put, run, env
from datetime import datetime
from os.path import exists
from fabric.network import disconnect_all

env.hosts = ['35.196.1.33', '35.243.140.125']


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


def do_deploy(archive_path):
    """deploy and uncompress file to server."""
    if not exists(archive_path):
        return False

    put(archive_path, "/tmp/")
    name_of_file = archive_path.split('/')[-1]
    name = name_of_file.split('.')[0]  # name withouth extension.
    final_path = "/data/web_static/releases/" + name
    run("mkdir -p " + final_path)
    run("tar -xzf /tmp/" + name_of_file + " -C " + final_path)
    run("rm /tmp/" + name_of_file)

    run("mv " + final_path + "/web_static/* " + final_path)
    run("rm -rf /data/web_static/current")
    run("rm -rf " + final_path + "/web_static/")
    run("ln -s {} /data/web_static/current".format(final_path))

    disconnect_all()

    return True

#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of the web_static
# folder of your AirBnB Clone repo, using the function do_pack.

from fabric import task
from fabric.api import local
from datetime import datetime


def do_pack():
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        archive_name = f"web_static_{timestamp}.tgz"
        archive_path = f"versions/{archive_name}"

        local("mkdir -p versions")

        result = local(f"tar -czvf {archive_path} web_static")
        return archive_path

    except Exception as e:
        return None

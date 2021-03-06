# -*- coding: utf-8 -*-
from ploceus.tools import files

def directory(path, user=None, grp=None,
              mode=None, recursive=False, use_sudo=None):

    if not files.is_dir(path):
        files.mkdir(path, user=user, grp=grp,
                    use_sudo=use_sudo)
        return

    if (user and (files.owner(path) != user)) or\
       ((grp and files.group(path) != grp)):
        files.chown(path, user=user, grp=grp,
                    recursive=recursive, use_sudo=use_sudo)

    if mode and (files.mode(path) != mode):
        files.chmod(path, mode=mode, recursive=recursive,
                    use_sudo=use_sudo)

def file(path, user=None, grp=None,
         mode=None, use_sudo=None):

    if (user and (files.owner(path) != user)) or\
       ((grp and files.group(path) != grp)):
        files.chown(path, user=user, grp=grp,
                    use_sudo=use_sudo)

    if mode and (files.mode(path) != mode):
        files.chmod(path, mode=mode,
                    use_sudo=use_sudo)

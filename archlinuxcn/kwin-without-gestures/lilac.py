#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    update_pkgver_and_pkgrel(_G.newver.split("-", 1)[0])

def post_build():
    git_pkgbuild_commit()
    update_aur_repo()

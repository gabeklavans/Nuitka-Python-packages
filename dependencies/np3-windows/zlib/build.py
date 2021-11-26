import __np__
from typing import *

import os
import shutil


def run(temp_dir: str):
    __np__.download_extract("https://zlib.net/zlib1211.zip", temp_dir)

    __np__.setup_compiler_env()

    __np__.auto_patch_MD_MT(os.path.join(temp_dir, "zlib-1.2.11", "win32"))

    os.chdir(os.path.join(temp_dir, "zlib-1.2.11"))

    __np__.nmake("/f", "win32/Makefile.msc")

    __np__.install_dep_libs("zlib", os.path.join(temp_dir, "zlib-1.2.11", "zlib.lib"))
    __np__.install_dep_include("zlib", os.path.join(temp_dir, "zlib-1.2.11", "*.h"))

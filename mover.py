#!/usr/bin/env python

import shutil
import os

source = "$HOME/devel/test/"
destination = "$HOME/devel/test/dest/"

filenames = os.listdir(source)

for name in filenames:
    if name.endswith(".txt"):
        print("Moving %s to %s") % (name, destination)
        shutil.move(os.path.join(source, name), destination)

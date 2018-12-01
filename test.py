## -*- coding: utf-8 -*-

import os
from fnmatch import fnmatch


root = '/home/ivliev/Рабочий стол/face_id_ros/info'
pattern = "*.jpg"

for path, subdirs, files in os.walk(root):
    for name in subdirs:
        #if fnmatch(name, pattern):
        #print name #(os.path.join(path, name))
        for path2, subdirs2, files2 in os.walk(os.path.join(path, name)):
            for name2 in files2:
                if fnmatch(name2, pattern):
                    print name2

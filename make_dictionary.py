# python3 make_id_finish6.py  -m 'w' -t 'ID.txt'
## -*- coding: utf-8 -*-


try:
    import cPickle as pickle
except ImportError:
    import pickle
import argparse
import dlib
from imutils import face_utils
from skimage import io
from scipy.spatial import distance
import numpy as np
import copy
import time
import cv2
import imutils
import os
import fnmatch
import os
from fnmatch import fnmatch


def index_min(array, n):
    array_new=[]
    for i in range(len(array)):
        array_new.append(array[i][n])
    minimym = min(array_new)
    index=array_new.index(minimym)
    return minimym, index

def index_max(array, n):
    array_new=[]
    for i in range(len(array)):
        array_new.append(array[i][n])
    maximym = max(array_new)
    indexmax=array_new.index(maximym)
    return maximym, indexmax


def rect_to_bb(rect):
	x = rect.left()
	y = rect.top()
	w = rect.right() - x
	h = rect.bottom() - y
	return (x, y, w, h)

def get_face_descriptor(imge):    # from image
    img = io.imread(imge)
    dets = detector(img, 1)
    for k, d in enumerate(dets):
        shape = predictor(img, d)
    face_descriptor = facerec.compute_face_descriptor(img, shape)
    return face_descriptor

 
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat') 

array_name=[]
dictionary=[]

i=0
# read from file
root = '/home/ivliev/Рабочий стол/face_id_ros/info'
pattern = "*.jpg"

for path, subdirs, files in os.walk(root):
	for name in subdirs:
		#if fnmatch(name, pattern):
		#print name #(os.path.join(path, name))
		for path2, subdirs2, files2 in os.walk(os.path.join(path, name)):
			for name2 in files2:
				if fnmatch(name2, pattern):
					dir_name2=(os.path.join(path2, name2))
					print dir_name2
					dictionary.append([[],[],[]])
					dictionary[i][0]=name
					dictionary[i][1]=np.array(get_face_descriptor(dir_name2))
					dictionary[i][2]=0
					i+=1
"""
os.chdir('info/')
for file in os.listdir('.'):
	if fnmatch.fnmatch(file, '*.jpg'):
		name=os.path.splitext(file)[0]

		dictionary.append([[],[],[]])
		dictionary[i][0]=name
		dictionary[i][1]=np.array(get_face_descriptor(str(name)+'.jpg'))
		dictionary[i][2]=0
		#print dictionary[i][1]

		array_name.append(name)
		print(name+'.jpg')
		i+=1

os.chdir('..')
"""

#with open("dictionary.pkl","wb") as f:
f=open("dictionary.pkl","wb")
for i in range(len(dictionary)):
	pickle.dump(dictionary[i], f)
f.close()



d = open("dictionary.txt", "w")
for i in range(len(dictionary)):
	s=str(dictionary[i])
	d.write(s+ '\n')
	d.write('\n')
d.close()

## -*- coding: utf-8 -*-

import pickle
import numpy as np
from scipy.spatial import distance


face_base = []
with open("dictionary.pkl", "rb") as f:

	
	#p = pickle.load(f)
	#print(p)
	
	
	try:
	
		while True:
			face_base.append(pickle.load(f))

	except (EOFError, pickle.UnpicklingError):
		pass
	
x=distance.euclidean(face_base[0][1], face_base[1][1])


print x
print (face_base[0][0],face_base[1][0])

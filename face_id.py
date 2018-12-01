
# python3 seve_deskriptor.py
# python3 seve_deskriptor.py  --picamera 1

## -*- coding: utf-8 -*-


from skimage import io
from imutils.video import VideoStream
from imutils import face_utils
from scipy.spatial import distance
import numpy as np
import datetime
import argparse
import imutils
import dlib
import time
import cv2
import cPickle as pickle



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


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat') 

face_base = []

with open("dictionary.pkl", "rb") as f:
	face_base = []
	try:
	
		while True:
			face_base.append(pickle.load(f))

	except (EOFError, pickle.UnpicklingError):
		pass


print "trew"

print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()


ap = argparse.ArgumentParser()
ap.add_argument("-p", "--picamera", type=int, default=-1,
	help="use pi camera")

args = vars(ap.parse_args())


vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)

while True:
	frame = vs.read()

	frame = imutils.resize(frame, width=600)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


	rects = detector(gray, 0)
	cv2.imshow("Frame", frame)
	
	max_face=[]

	# loop over the face detections
	if (len(rects)>0):

		i=0
		for rect in rects:
			shape_cam = predictor(gray, rect)
			shape2 = face_utils.shape_to_np(shape_cam)

			# loop over the (x, y)-coordinates for the facial landmarks
			# and draw them on the image
			for (x, y) in shape2:
				cv2.circle(frame, (x, y), 0, (0, 255, 255), -1)
	    
			cv2.imshow("Frame", frame)
			
			x, y, w, h = rect_to_bb(rect)
			max_face.append([[],[]])
			max_face[i][0]=rect
			max_face[i][1]=w*h

			
			i+=1


		maximym, indexmax = index_max(max_face,1)

		shape_cam = predictor(gray, max_face[indexmax][0])
		shape2 = face_utils.shape_to_np(shape_cam)

		
		face_descriptor_cam= facerec.compute_face_descriptor(frame, shape_cam)

		for i in range(len(face_base)):
			face_base[i][2]=distance.euclidean(face_base[i][1], face_descriptor_cam)
		minimym, index =index_min(face_base,2)
		if (minimym < 0.5):
			print(face_base[index][0])

	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
        	# do a bit of cleanup
		cv2.destroyAllWindows()
		vs.stop()




import pickle

dictionary=[1,1,1,1,1,1,1,1111,111,1,"45678900uhubjnk",[1,1]]

#with open("dictionary.pkl","wb") as f:
f=open("dictionary.pkl","wb")
for i in range(len(dictionary)):
	pickle.dump(dictionary[i], f)
f.close()

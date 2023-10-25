import numpy as np 
import cv2 
import os 
import random 
import matplotlib as plt 
import pickle 
direc="E:\\hac\\ext-data"
nfile="E:\\hac\\name of the animals.txt"
file=open(nfile,'r')
category=[]
g=1
for i in file:
    s=i.split("\n")
    category.append(s[0])

img_size=100
data=[]
for i in category:
    folder=os.path.join(direc,i)
    label=category.index(i)
    for img in os.listdir(folder):
        img_path=os.path.join(folder,img)
        img_arr=cv2.imread(img_path)
        img_arr=cv2.resize(img_arr,(img_size,img_size)) 
        data.append([img_arr,label])

x=[]
y=[]
for features,labels in data:
    x.append(features)
    y.append(labels)

pickle.dump(x,open("x.pkl",'wb'))
pickle.dump(y,open("y.pkl",'wb'))
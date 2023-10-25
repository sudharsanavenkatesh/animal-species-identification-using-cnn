import pickle
import cv2 as cv 

def pred(piv):
    name="F:\\hac\\flak"+'\\'+piv
    pict=cv.imread(name)
    pict=cv.resize(pict,(100,100))
    i=pict.reshape((1,100,100,3))
    g=mod.predict(i)
    g=g.tolist()
    g=[int(i) for i in g[0]]
    if max(g)==0:
        return "sorry we couldn't find the image"
    ind=g.index(max(g))
    return category[ind]
with open('model_pickle','rb') as f:
    mod=pickle.load(f)

nfile="F:\\hac\\name of the animals.txt"
file=open(nfile,'r')
category=[]
g=1
for i in file:
    s=i.split("\n")
    category.append(s[0])

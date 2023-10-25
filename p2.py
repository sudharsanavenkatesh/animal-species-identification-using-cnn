
import pickle 
from keras.models import Sequential
from keras.layers import Dense,Conv2D,MaxPooling2D,Flatten,BatchNormalization,Dropout
import numpy as np

x=pickle.load(open('x.pkl','rb'))
y=pickle.load(open('y.pkl','rb'))
for i in range(0,len(x)):
        x[i]=x[i]/255


model = Sequential()

model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D(2,2))

model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D(2,2))

model.add(Flatten())

model.add(Dense(128,input_shape=x[0].shape[1:],activation='relu'))

model.add(Dense(100,activation='softmax'))
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

x=np.array(x)

y=np.array(y)

model.fit(x,y,batch_size=32,epochs=10,validation_split=0.1)

with open('model_pickle','wb') as f:
        pickle.dump(model,f)

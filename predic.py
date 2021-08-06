'''

'''

import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator


test_datagen = ImageDataGenerator(rescale=1./255,fill_mode='constant')

x_predict = np.load('./_npy/x_predict.npy')
x_train = np.load('./_npy/x_train.npy')
y_train = np.load('./_npy/y_train.npy')
x_test = np.load('./_npy/x_test.npy')
y_test = np.load('./_npy/y_test.npy')

print(y_train.shape)
print(y_test.shape)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,Dense,Flatten,Dropout,MaxPool2D,AveragePooling2D
import time

'''
걸린시간 1892.8494307994843
'''
model = Sequential()
model.add(Conv2D(64,(2,2),padding='same',activation='relu',input_shape=(150,150,3)))
model.add(AveragePooling2D(2,2)) # 정해진 범위안에서 큰값만 뽑아냄
model.add(Conv2D(32,(2,2),padding='same',activation='relu'))
model.add(AveragePooling2D(2,2))
model.add(Conv2D(16,(2,2),padding='same',activation='relu'))
model.add(AveragePooling2D(2,2))
model.add(Flatten())
model.add(Dense(32,activation='relu'))
model.add(Dense(16,activation='relu'))
model.add(Dense(7,activation='softmax'))
'''
(16156, 150, 150, 3)
(16156, 7)
'''
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
es = EarlyStopping(monitor='val_acc', patience=10, mode='max', verbose=1)

starttime = time.time()
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['acc'])
hist = model.fit(x_train,y_train,epochs=100,batch_size=128, validation_data=(x_test,y_test),callbacks=[es])
'''
Maxpool적용
loss 0.9999203681945801 입니다
[[4.3507567e-12 5.8444487e-21 1.2658714e-13 4.5635996e-16 2.4035138e-12
  3.8606544e-17 1.0000000e+00]]
acc는 :  0.9999203681945801 입니다
농산물6.jpeg 는 :  93.4 %의 확률로  토마토 입니다

Averagepool적용
loss 0.9999203681945801 입니다
[[0.0000000e+00 0.0000000e+00 1.2311623e-29 3.1023863e-30 1.4640748e-34
  0.0000000e+00 1.0000000e+00]]
acc는 :  0.9999203681945801 입니다
농산물6.jpeg 는 :  91.60000000000001 %의 확률로  토마토 입니다
'''

loss = model.evaluate(x_test, y_test) 
y_predic = model.predict(x_predict)
acc = hist.history['acc']
val_acc = hist.history['val_acc']
loss = hist.history['loss']
val_loss = hist.history['val_loss']
end = time.time()- starttime
print('loss',acc[-1],'입니다')

print(y_predic)

class_pred = ''
for i in y_predic:
        max_temp = i.argmax()
        if max_temp == 0 : class_pred = '사과'
        elif max_temp == 1 : class_pred = '한라봉' 
        elif max_temp == 2 : class_pred = '감귤' 
        elif max_temp == 3 : class_pred = '적양파' 
        elif max_temp == 4 : class_pred = '양파' 
        elif max_temp == 5 : class_pred = '감자' 
        elif max_temp == 6 : class_pred = '토마토' 
        
import matplotlib.pyplot as plt
import matplotlib.image as img
import glob
filename = []
predic_dir = '../_data/farm/predict' 
files = glob.glob(predic_dir + "/*/*.*") # 하위 디렉토리까지 반환, 하위디렉토리는 역슬래쉬로 바뀐다. 리스트형식으로 봔환
print(files)
#['../_data/farm/predict\\x_predict\\농산물6.jpeg']

for i,f in enumerate(files):
    filename.append(f)

name = filename[0].split('\\')[2] # 문자를 나누는 기호
path = '../_data/farm/predict/x_predict/'+name
predic_img = img.imread(path,1) # color
 
print("걸린시간", end)
print('acc는 : ',acc[-1],'입니다')
print(name,'는 : ',round(val_acc[-1],3) * 100,'%의 확률로 ',class_pred,'입니다')
plt.imshow(predic_img)
plt.title(name+' 은 '+class_pred+'입니다')
plt.show()
'''

'''

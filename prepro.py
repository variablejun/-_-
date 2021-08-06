import numpy as np
import time
from tensorflow.keras.preprocessing.image import ImageDataGenerator
starttime = time.time()

train_datagen = ImageDataGenerator(rescale=1./255,fill_mode='constant')
test_datagen = ImageDataGenerator(rescale=1./255,fill_mode='constant')

xy_train = train_datagen.flow_from_directory('../_data/farm/train',target_size=(150,150),batch_size=12554
,shuffle=False,class_mode='categorical') 

xy_test = test_datagen.flow_from_directory('../_data/farm/test',target_size=(150,150),batch_size=1600
,shuffle=False,class_mode='categorical')

'''

'''

print(xy_train[0][0].shape)
print(xy_train[0][1].shape)
print(xy_train[0][0].shape)
print(xy_train[0][1].shape)
'''
np.save('./_npy/x_train.npy',arr=xy_train[0][0])
np.save('./_npy/y_train.npy',arr=xy_train[0][1])
np.save('./_npy/x_test.npy',arr=xy_test[0][0])
np.save('./_npy/y_test.npy',arr=xy_test[0][1])
'''
end = time.time()- starttime
print("걸린시간", end)

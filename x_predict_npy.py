

import numpy as np
import time
from tensorflow.keras.preprocessing.image import ImageDataGenerator
test_datagen = ImageDataGenerator(rescale=1./255,fill_mode='constant')

x_predic = test_datagen.flow_from_directory('../_data/farm/predict',target_size=(150,150),
shuffle=False,class_mode='categorical')

np.save('./_npy/x_predict.npy',arr=x_predic[0][0])


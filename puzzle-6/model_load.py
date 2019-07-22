import json
import keras
from keras.models import model_from_json
from keras.datasets import cifar100
from keras.models import Model
from keras.layers import Dense, Dropout, Flatten, Input, Concatenate, BatchNormalization, Add
from keras.layers import Conv2D, MaxPooling2D, ReLU
from keras import backend as K
import numpy as np

batch_size = 64
num_classes = 100
epochs = 100

# input image dimensions
img_rows, img_cols, channels = 32, 32, 3

# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = cifar100.load_data()

x_train = x_train[:len(x_test)]
y_train = y_train[:len(y_test)]

if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], channels, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], channels, img_rows, img_cols)
    input_shape = (channels, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, channels)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, channels)
    input_shape = (img_rows, img_cols, channels)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
# y_train = keras.utils.to_categorical(y_train, num_classes)
# y_test = keras.utils.to_categorical(y_test, num_classes)

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")
 
# evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

train_predicts = loaded_model.predict(x_train)
test_predicts = loaded_model.predict(x_test)

print(train_predicts[0,:])
print(train_predicts[1,:])
print(train_predicts[2,:])
print(train_predicts[3,:])



y_train[:,0] = 0
y_test[:, 0] = 1

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, 2)
y_test = keras.utils.to_categorical(y_test, 2)

print(y_train.shape)


new_x_train = np.vstack((train_predicts[:9000, :], test_predicts[:9000, :]))
new_y_train = np.vstack((y_train[:9000, :], y_test[:9000, :]))

new_x_test = np.vstack((train_predicts[9000:, :], test_predicts[9000:, :]))
new_y_test = np.vstack((y_train[9000:, :], y_test[9000:, :]))



############################# Architecture made by Ennui
x0 = Input(shape=(100,))
x15 = BatchNormalization(momentum=0.99)(x0)
x8 = Dense(2048, activation='relu')(x15)
x7 = Dropout(0.5)(x8)
x4 = Dense(1024, activation='relu')(x7)
x5 = Dropout(0.5)(x4)
x3 = Dense(512, activation='relu')(x5)
x2 = Dropout(0.5)(x3)

x10 = Dense(256, activation='relu')(x2)
x11 = Dropout(0.5)(x10)

x12 = Dense(128, activation='relu')(x11)
x13 = Dropout(0.5)(x12)

x1 = Dense(2, activation='softmax')(x13)
model = Model(inputs=x0, outputs=x1)
#############################

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adam(lr=0.0008),
              metrics=['accuracy'])

model.fit(new_x_train, new_y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(new_x_test, new_y_test))
score = model.evaluate(new_x_test, new_y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# serialize model to JSON
model_json = model.to_json()
with open("model-new.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model-new.h5")
print("Saved model to disk")
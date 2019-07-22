from __future__ import print_function
import keras
from keras.datasets import cifar100
from keras.models import Model
from keras.layers import Dense, Dropout, Flatten, Input, Concatenate, BatchNormalization, Add
from keras.layers import Conv2D, MaxPooling2D, ReLU
from keras import backend as K

batch_size = 64
num_classes = 100
epochs = 15

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
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

############################# Architecture made by Ennui
x0 = Input(shape=input_shape)
x2 = Conv2D(64, (3,3), strides=(1,1), activation='relu', padding='same')(x0)
x5 = Conv2D(64, (3,3), strides=(1,1), activation='relu')(x2)
x6 = MaxPooling2D(pool_size=(2,2), strides=(2,2))(x5)
x7 = Flatten()(x6)
x8 = Dense(512, activation='relu')(x7)
x4 = Dense(256, activation='relu')(x8)
x1 = Dense(100, activation='softmax')(x4)
model = Model(inputs=x0, outputs=x1)
#############################

print(model.summary())

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adam(lr=0.0001),
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")





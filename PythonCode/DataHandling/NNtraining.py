import numpy as np
import statistics as stats
import time

#Neural Net specifics:
import tensorflow
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import backend as K
from tensorflow.keras.layers import Dense, Dropout, Flatten

class NeuralNet:

    # Loading in all parameters
    # Also data read in and preparation
    def __init__(self):
        print("Num GPUs Available: ", len(tensorflow.config.experimental.list_physical_devices('GPU')))

        self.img_rows = 480
        self.img_cols = 640

        self.batch_size = 128
        self.epochs = 2000

        self.data_x = []
        self.data_y = []

        self.x_train = []
        self.y_train = []
        self.x_test = []
        self.y_test = []

    def train_model(self, salinity_arr, img_arr, model_name):
        self.read_in_data(salinity_arr, img_arr)
        self.data_prep("Naive")
        input_shape = self.reshape_and_input_size(if_gray="False")
        model = self.compile_model(input_shape=input_shape, if_print_model_summary=False)
        self.fit_the_model(model=model, model_name=model_name, if_image_aug=False)

    def read_in_data(self, data_arr, img_arr):
        self.data_x = np.array(img_arr)
        for n in range(len(data_arr)):
            self.data_y.append(stats.variance(data_arr[n]))
        #print(self.data_x)
        #print(self.data_y)

    #Choose mode wisely. Guide to modes:
    #1. "Naive" - all data both in training and testing
    def data_prep(self, mode):
        if mode == "Naive":
            self.x_train = np.array(self.data_x, dtype=np.float32)
            self.x_test = np.array(self.data_x, dtype=np.float32)
            self.x_train /= 255
            self.x_test /= 255
            print('x_train shape:', self.x_train.shape)
            print(self.x_train.shape[0], 'train samples')
            print(self.x_test.shape[0], 'test samples')
            # Now y is taken care of
            self.y_train = np.array(self.data_y, dtype=np.float32)
            self.y_test = np.array(self.data_y, dtype=np.float32)
            #Downscaling the data, so it's in 0-1 range, factor of 30 used here
            self.y_train /= 30.
            self.y_test /= 30.

    #It will reshape training and test pictures if needed
    #Gray option available, but not to be used with VGA model
    def reshape_and_input_size(self, if_gray):
        if if_gray != "True":
            if K.image_data_format() == 'channels_first':
                self.x_train = self.x_train.reshape(self.x_train.shape[0], 3, self.img_rows, self.img_cols)
                self.x_test = self.x_test.reshape(self.x_test.shape[0], 3, self.img_rows, self.img_cols)
                return (3, self.img_rows, self.img_cols)
            else:
                self.x_train = self.x_train.reshape(self.x_train.shape[0], self.img_rows, self.img_cols, 3)
                self.x_test = self.x_test.reshape(self.x_test.shape[0], self.img_rows, self.img_cols, 3)
                return (self.img_rows, self.img_cols, 3)
        else:
            if K.image_data_format() == 'channels_first':
                self.x_train = self.x_train.reshape(self.x_train.shape[0], 1, self.img_rows, self.img_cols)
                self.x_test = self.x_test.reshape(self.x_test.shape[0], 1, self.img_rows, self.img_cols)
                return (1, self.img_rows, self.img_cols)
            else:
                self.x_train = self.x_train.reshape(self.x_train.shape[0], self.img_rows, self.img_cols, 1)
                self.x_test = self.x_test.reshape(self.x_test.shape[0], self.img_rows, self.img_cols, 1)
                return (self.img_rows, self.img_cols, 1)

    def compile_model(self, input_shape, if_print_model_summary):
        model = VGG16(include_top=False, weights='imagenet', input_shape=input_shape, pooling="max")
        for layer in model.layers:
            layer.trainable = False
        dropout1 = Dropout(0.2)(model.layers[-1].output)
        class1 = Dense(600, activation='sigmoid')(dropout1)
        dropout2 = Dropout(0.2)(class1)
        class2 = Dense(300, activation='sigmoid')(dropout2)
        dropout3 = Dropout(0.2)(class2)
        class3 = Dense(600, activation='sigmoid')(dropout3)
        output = Dense(1, activation='linear')(class3)
        model = Model(inputs=model.inputs, outputs=output)
        model.compile(loss=tensorflow.keras.losses.mean_squared_error, optimizer=tensorflow.keras.optimizers.Adadelta(),
                      metrics=tensorflow.keras.metrics.MeanAbsolutePercentageError())
        if if_print_model_summary == True:
            model.summary()
            for layer in model.layers:
                print(str(layer.trainable))

        return model

    #This part trains the network
    def fit_the_model(self, model, model_name, if_image_aug):
        if model == None:
            print("No model presented for train_model")
            return
        if if_image_aug == True:
            datagen = ImageDataGenerator(rotation_range=20,width_shift_range=0.2,height_shift_range=0.2,horizontal_flip=True,   featurewise_center = True)
            self.model_for_history = model.fit(datagen.flow(self.x_train, self.y_train, batch_size=self.batch_size), epochs=self.epochs, verbose=1, validation_data=(self.x_test, self.y_test))
        else:
            self.model_for_history = model.fit(self.x_train, self.y_train, batch_size=self.batch_size, epochs=self.epochs, verbose=1, validation_data=(self.x_test, self.y_test))
        score = model.evaluate(self.x_test, self.y_test, verbose=0)
        print('Test loss:', score[0])
        print('Test accuracy:', score[1])
        model.save("Trained_Models/" + str(model_name) + ".h5")
from __future__ import absolute_import, division, print_function, unicode_literals

import os
import sys
import logging

from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model

from keras.constraints import maxnorm

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, models
import tensorflow.keras.optimizers as Optimizer

from keras.preprocessing.image import ImageDataGenerator

import cv2 as cv
import numpy as np
from random import randint
from pathlib import Path

import urllib.request
import time
from PIL import Image


class ImageService:

    model = None
    # def train(self):
    #     model = self.newModel1()
    #     trainDataGenerator = ImageDataGenerator(
    #         rescale=1./255,
    #         shear_range=0.2,
    #         zoom_range=0.2,
    #         horizontal_flip=True
    #     )

    #     dir = os.path.dirname(__file__)
    #     testDataGenerator = ImageDataGenerator(rescale=1./255)

    #     trainingSet = trainDataGenerator.flow_from_directory(
    #         os.path.join(dir, '..', 'images', 'training'),
    #         target_size=(100, 180),
    #         batch_size=8,
    #         class_mode='sparse'
    #     )

    #     testSet = trainDataGenerator.flow_from_directory(
    #         os.path.join(dir, '..', 'images', 'test'),
    #         target_size=(100, 180),
    #         batch_size=8,
    #         class_mode='sparse'
    #     )

    #     model.fit_generator(
    #         trainingSet,
    #         steps_per_epoch=170,
    #         epochs=25,
    #         validation_data=testSet,
    #         validation_steps=25
    #     )

    #     self.saveModel(model)

    # def newModel1(self):
    #     model = models.Sequential()
    #     model.add(layers.Conv2D(16, 3, 3, activation='relu',
    #                             input_shape=(100, 180, 3)))
    #     model.add(layers.Conv2D(32, 2, 2, padding='same', activation='relu'))
    #     model.add(layers.Conv2D(64, 3, 3, padding='same', activation='relu'))
    #     model.add(layers.Conv2D(128, 3, 3, padding='same', activation='relu'))

    #     model.add(layers.MaxPooling2D(pool_size=(2, 2)))

    #     model.add(layers.Flatten())
    #     # model.add(layers.Dropout(0.2))

    #     model.add(layers.Dense(128, activation="relu"))
    #     model.add(layers.Dense(2, activation="sigmoid"))

    #     model.compile(
    #         optimizer='adam',
    #         loss=['sparse_categorical_crossentropy'],
    #         metrics=['accuracy']
    #     )

    #     # model.compile(optimizer=Optimizer.Adam(),
    #     #               loss='binary_crossentropy', metrics=['accuracy'])
    #     return model

    def train(self):
        model = self.newModel1()
        trainDataGenerator = ImageDataGenerator(
            rescale=1./255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True
        )

        dir = os.path.dirname(__file__)
        testDataGenerator = ImageDataGenerator(rescale=1./255)

        trainingSet = trainDataGenerator.flow_from_directory(
            os.path.join(dir, '..', 'images', 'training'),
            target_size=(100, 180),
            batch_size=8,
            class_mode='binary'
        )

        testSet = trainDataGenerator.flow_from_directory(
            os.path.join(dir, '..', 'images', 'test'),
            target_size=(100, 180),
            batch_size=8,
            class_mode='binary'
        )

        model.fit_generator(
            trainingSet,
            steps_per_epoch=150,
            epochs=25,
            validation_data=testSet,
            validation_steps=25
        )

        self.saveModel(model)

    def newModel1(self):
        model = models.Sequential()
        model.add(layers.Conv2D(16, 3, 3, activation='relu',
                                input_shape=(100, 180, 3)))
        model.add(layers.Conv2D(32, 2, 2, padding='same', activation='relu'))
        model.add(layers.Conv2D(64, 3, 3, padding='same', activation='relu'))
        model.add(layers.Conv2D(128, 3, 3, padding='same', activation='relu'))

        model.add(layers.MaxPooling2D(pool_size=(2, 2)))

        model.add(layers.Flatten())
        # model.add(layers.Dropout(0.2))

        model.add(layers.Dense(128, activation="relu"))
        model.add(layers.Dense(1, activation="sigmoid"))

        model.compile(optimizer=Optimizer.Adam(),
                      loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def newModel(self):
        model = models.Sequential()
        model.add(layers.Conv2D(32, 3, 3, activation='relu',
                                input_shape=(100, 180, 3)))
        # model.add(layers.Dropout(0.2))
        # model.add(layers.BatchNormalization())
        # model.add(layers.Conv2D(64, (3, 3), padding='same', activation='relu'))
        model.add(layers.MaxPooling2D(pool_size=(2, 2)))
        # model.add(layers.Dropout(0.2))
        # model.add(layers.BatchNormalization())

        # model.add(layers.Conv2D(128, (3, 3), padding='same'))
        # model.add(layers.Activation('relu'))
        # model.add(layers.Dropout(0.2))
        # model.add(layers.BatchNormalization())

        model.add(layers.Flatten())
        # model.add(layers.Dropout(0.2))

        model.add(layers.Dense(128, activation="relu"))
        model.add(layers.Dense(1, activation="sigmoid"))

        # model.add(layers.Dense(256, kernel_constraint=maxnorm(3)))
        # model.add(layers.Activation('relu'))
        # model.add(layers.Dropout(0.2))
        # model.add(layers.BatchNormalization())

        # model.add(layers.Dense(128, kernel_constraint=maxnorm(3)))
        # model.add(layers.Activation('relu'))
        # model.add(layers.Dropout(0.2))
        # model.add(layers.BatchNormalization())

        # model.add(layers.Dense(180))
        # model.add(layers.Activation('softmax'))

        # model.compile(optimizer=Optimizer.Adam(),
        #               loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        model.compile(optimizer=Optimizer.Adam(),
                      loss='binary_crossentropy', metrics=['accuracy'])

        return model

    def saveModel(self, model):
        model.save('deku_model.h5')
        self.model = model

    def loadModel(self):
        model = tf.keras.models.load_model('deku_model.h5')
        model.summary()
        self.model = model

        return model

    def predict(self, url):
        if self.model == None:
            self.loadModel()

        fileName = "/tmp/%.20f" % time.time()
        urllib.request.urlretrieve(url, fileName + ".jpg")

        im = Image.open(fileName + ".jpg")
        size = 180, 100
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(fileName + ".thumbnail", "JPEG")

        img = self.loadImage(
            fileName + ".thumbnail")
        result = self.model.predict_proba(img)

        os.remove(fileName + ".thumbnail")
        os.remove(fileName + ".jpg")

        if result[0][0] <= 0.5:
            logging.debug('nice')
        else:
            logging.debug('ugly')

        return result[0][0]


    def loadImage(self, filename):
        img = load_img(filename, target_size=(100, 180))
        img = img_to_array(img)
        img = np.expand_dims(img, axis=0)
        return img

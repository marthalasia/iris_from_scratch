# -*- coding: utf-8 -*-
import numpy
import os
from pathlib import Path
from sklearn.externals import joblib


class IrisClassifier:

    def __init__(self, model_name):
        cwd = os.path.dirname(os.path.join(os.path.abspath("../"), "iris_101/"))
        #cwd = os.path.dirname(os.path.abspath("iris_101/"))
        self.path = Path(cwd + "/models/" + model_name)
        print(self.path)

    def predict(self, data):
        data = numpy.array(data)
        model = self.load_model()
        prediction = []
        if model is not None:
            prediction = self.load_model().predict(data)
        return prediction

    def load_model(self):
        model = None
        if self.path.exists():
            with open(self.path, 'rb') as file:
                model = joblib.load(file)
        return model


import config
import pickle
import numpy as np


class IrisPrediction():
    def __init__(self,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm):
        self.SepalLengthCm = SepalLengthCm
        self.SepalWidthCm = SepalWidthCm
        self.PetalLengthCm = PetalLengthCm
        self.PetalWidthCm = PetalWidthCm
        

    def load_model(self):
        
        with open(config.path,'rb') as f :
            self.lg_model = pickle.load(f)

    def predict(self):
        self.load_model()
        test = np.zeros(4)
        test[0] = self.SepalLengthCm
        test[1] = self.SepalWidthCm
        test[2] = self.PetalLengthCm
        test[3] = self.PetalWidthCm

        flower = self.lg_model.predict([test])[0]
        return flower


if __name__ == '__main__':
    ob = IrisPrediction(4.5,2.8,4.3,5)
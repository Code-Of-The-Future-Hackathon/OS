import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from fastapi import APIRouter
import tensorflow as tf
import numpy as np
import pandas as pd
import os
import json
import matplotlib.pyplot as plt
import keras

class Model:
    def __init__(self):
        self.model = keras.models.load_model("./models/landslide.keras")

    def predict(self, data: dict):
        # Convert data to numpy array
        dataL = np.array(list(data.values()))

        # Predict        
        prediction = self.model.predict(tf.expand_dims(dataL, axis=0), verbose=1)

        # Convert prediction to a list
        prediction = prediction.tolist()

        # Return prediction
        return prediction

model = Model()

router = APIRouter()

@router.post("/landslide", tags=["Landslide"])
async def predict(body: dict):
    prediction = model.predict(body)

    return {"prediction": prediction}
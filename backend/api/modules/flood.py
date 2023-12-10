import numpy as np
import tensorflow as tf
from fastapi import APIRouter

class Model:
    model: tf.keras.Model = None

    def __init__(self):
        self.model = tf.saved_model.load("./models/flood.keros")

    def predict(self, data: dict):
        # Convert data to numpy array
        data = np.array([data["data"]])

        # Predict
        prediction = self.model.predict(data)

        # Convert prediction to a list
        prediction = prediction.tolist()

        # Return prediction
        return prediction

model = Model()

router = APIRouter()

@router.post("/flood", tags=["Flood"])
async def predict(body: dict):
    prediction = model.predict(body)

    return {"prediction": prediction}
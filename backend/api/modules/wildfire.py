import numpy as np
from fastapi import APIRouter
import tensorflow as tf

class Model:
    model: tf.keras.Model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1)
    ])

    def __init__(self):
        self.model = tf.keras.models.load_model("./models/wildfire.keras")

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

@router.post("/wildfire", tags=["Wildfire"])
async def predict(body: dict):
    prediction = model.predict(body)

    return {"prediction": prediction}
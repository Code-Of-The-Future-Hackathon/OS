import tensorflow as tf
import numpy as np
import pandas as pd
import os
import json
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import keras

# Load your training data
with open('../../training_data/drought_training_data.json', 'r') as file:
    training_data = json.load(file)

df = pd.DataFrame(training_data)

# Separate features and target variable
X = df[['temperature', 'relative_humidity', 'dewpoint', 'precipitation', 'wind_speed', 'cloud_cover', 'soil_moisture']].values
y = df['is_drought'].values

# Normalize features using the mean and std from the entire dataset
X_normalized = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size=0.3, random_state=42)

# Define and train the model with more complex architecture
model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, input_shape=(7,), activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='linear')
])

model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.001), loss='mse', metrics=["accuracy"])

model.fit(X_train, y_train, epochs=1500, verbose=1)

keras.models.save_model(model, filepath="../drought.keras", save_format="tf")
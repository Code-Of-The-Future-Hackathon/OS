import tensorflow as tf
import numpy as np
import pandas as pd
import os
import json
import random
import matplotlib.pyplot as plt

with open('training data.json', 'r') as file:
    training_data = json.load(file)

df = pd.DataFrame(training_data)

df = df.sample(frac=1).reset_index(drop=True)

features = df.drop(['precipitation', 'rain_intensity', 'soil_moisture', 'wind_speed', 'relative_humidity', 'temp_disparity', 'temperature', 'evapotranspiration'], axis=1).values
target = df['chance'].values

features = tf.constant(features, dtype=tf.float32)
target = tf.constant(target, dtype=tf.float32)

W = tf.Variable(tf.random.normal([8]))
b = tf.Variable(tf.random.normal([1]))

def linear_regression(x):
    return W * x + b

def mean_square(y_pred, y_true):
    return tf.reduce_mean(tf.square(y_pred - y_true))

optimizer = tf.optimizers.SGD(learning_rate=0.01)

for i in range(1000):
    with tf.GradientTape() as tape:
        y_pred = linear_regression(features)
        loss = mean_square(y_pred, target)
    gradients = tape.gradient(loss, [W, b])
    optimizer.apply_gradients(zip(gradients, [W, b]))

print(f'W = {W.numpy()}, b = {b.numpy()}')

plt.plot(features, target, 'ro', label='Original data')
plt.plot(features, np.array(W * features + b), label='Fitted line')
plt.legend()
plt.show()
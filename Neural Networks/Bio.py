import tensorflow as tf
import numpy as np
from tensorflow import keras as k
import matplotlib.pyplot as plt

# Dataset
from sklearn.datasets import load_diabetes
data = load_diabetes()
x, y = data['data'], data['target']

# Modello
modello = tf.keras.Sequential([
    k.layers.Dense(15, k.activations.relu, input_shape=(422,10)),
    k.layers.Dense(11, k.activations.relu),
    k.layers.Dense(1, k.activations.sigmoid)
])
print(modello.summary())

# Fit
modello.compile(optimizer=k.optimizers.Adam(),
                loss=k.losses.BinaryCrossentropy,
                metrics=k.metrics.binary_accuracy
                )

# Training
epochs = 15
modello.fit(x, y, epochs=epochs)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(range(epochs), modello.history.history['loss'])






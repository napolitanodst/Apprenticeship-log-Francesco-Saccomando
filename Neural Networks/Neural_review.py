import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np


# Dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()


# Modello
model = tf.keras.models.Sequential(
    [
       tf.keras.layers.Flatten(input_shape=(28, 28),),
       tf.keras.layers.Lambda(lambda x : x / 255.0),
       tf.keras.layers.Dense(35, activation="sigmoid", name="primo_layer"),
       tf.keras.layers.Dense(10, activation="softmax", name="ultimo_layer")
   ]
)
model.summary()

model.compile(
    optimizer=tf.keras.optimizers.SGD(),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=["accuracy"]
)

# Callback per visualizzare i pesi ad ogni epoch
weights_history = []
class WeightsHistory(keras.callbacks.Callback):
    def on_batch_end(self, batch, logs):
        weights = model.get_weights()
        w1, w2, w3, w4 = weights
        weights = [w1[0], w2[0], w3[0], w4[0]]
        weights_history.append(weights)

Weights = WeightsHistory()


# Training
history = model.fit(x_train, y_train, epochs=10, verbose=False, callbacks=[Weights])
loss, accuracy = model.evaluate(x_test, y_test)

print(weights_history)

plt.figure(1, figsize=(6, 3))
plt.plot(weights_history)
plt.show()
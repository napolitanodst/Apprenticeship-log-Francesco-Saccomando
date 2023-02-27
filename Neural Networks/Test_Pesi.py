import tensorflow as tf
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt

# Modello
model = tf.keras.Sequential(
    [
     tf.keras.layers.Dense(1, input_shape=(2,), activation='tanh', name="layer")
    ])

# Compiling
model.compile(
              tf.keras.optimizers.SGD(),
              loss=tf.keras.losses.MeanSquaredError(),
              metrics=["accuracy"]
)
#Training Data
def tanh(x):
    x_sum = np.sum(x)
    return np.tanh(x_sum)
train_data = np.random.random((500, 2))
train_labels = np.array(list(map(tanh, train_data)))

weights_history = []
class MyCallback(keras.callbacks.Callback):
    def on_batch_end(self, batch, logs):
        weights, _biases = model.get_weights()
        w1, w2 = weights
        weights = [w1[0], w2[0]]
        weights_history.append(weights)


callback = MyCallback()

# Fit
model.fit(train_data, train_labels, epochs=10,
          verbose=False, callbacks=[callback])

# Plot epoche
plt.figure(1, figsize=(6, 3))
plt.plot(weights_history)
plt.show()
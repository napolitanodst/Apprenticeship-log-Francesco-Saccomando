import pandas as pd
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
       tf.keras.layers.Rescaling(1./255),
       tf.keras.layers.Dense(10, activation="sigmoid", name="primo_layer"),
       tf.keras.layers.Dense(10, activation="softmax", name="output_layer")
   ]
)
model.summary()

model.compile(
    optimizer=tf.keras.optimizers.SGD(),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=["accuracy"]
)

# Callback per visualizzare i pesi ad ogni epoch
history_pesi =[]
class Epoche(keras.callbacks.Callback):
    def on_batch_end(self, batch, logs=None):
            weights = model.get_weights()[0]
            w1 = weights
            weights = [w1[0]]
            history_pesi.append(weights)


chiamata = Epoche()

# Training
history = model.fit(x_train, y_train, epochs=15, callbacks=chiamata)
loss, accuracy = model.evaluate(x_test, y_test)

plott = np.array(history_pesi)
plott_up = np.squeeze(plott)
epo = 10
#Plot dei pesi
plt.figure()
plt.plot(plott_up)
plt.title('Weights per epoch')
plt.show()

# Plot dell'accuracy
pd.DataFrame(history.history)[["accuracy",]].plot()








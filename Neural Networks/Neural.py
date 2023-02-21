import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
# Dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()


# Modello
model = tf.keras.models.Sequential(
    [
       tf.keras.layers.Flatten(input_shape=(28,28),),
       tf.keras.layers.Lambda(lambda x : x / 255.0),
       tf.keras.layers.Dense(56, activation="sigmoid", name="primo layer"),
       tf.keras.layers.Dense(10, activation="softmax", name="ultimo layer")
   ]
)
model.compile(
    optimizer= tf.keras.optimizers.SGD(),
    loss= tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics= ["accuracy"]
)
# Fit
history = model.fit (x_train,y_train,epochs=5, verbose=0)
loss, accuracy = model.evaluate(x_test, y_test)
pd.DataFrame(history.history)[["accuracy"]].plot()

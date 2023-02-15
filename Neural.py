import tensorflow as tf

# Dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()


# Modello
model = tf.keras.models.Sequential(
    [
       tf.keras.layers.Flatten(input_shape=(28,28),),
       tf.keras.layers.Lambda(lambda x : x / 255.0),
       tf.keras.layers.Dense(56, activation="sigmoid", name="neuroni_ingresso"),
       tf.keras.layers.Dense(10, activation="softmax", name="neuroni_uscita" )
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

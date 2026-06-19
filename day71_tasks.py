#Basic tensorflow
from numpy.testing import verbose
from tensorflow.keras.layers import Dense
import tensorflow as tf
import numpy as np

#First task
X = np.array([
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
    [4, 5, 6, 7],
    [5, 6, 7, 8],
    [6, 7, 8, 9]
], dtype=float)

y = np.array([
    0,
    0,
    0,
    1,
    1,
    1
])


model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(4,)),
    tf.keras.layers.Dense(
        16,
        activation='relu'
    ),
    tf.keras.layers.Dense(
        8,
        activation = 'relu'
    ),
    tf.keras.layers.Dense(
        1,
        activation = 'sigmoid'
    )
])

model.compile(
    optimizer = 'adam',
    loss = 'binary_crossentropy',
    metrics = ['accuracy']
)

model.summary()

model.fit(
    X,
    y,
    epochs = 100,
    verbose = 1
)

new_data = np.array([[7,8,9,10]])

prediction = model.predict(new_data)

print(f"Prediction probability: {prediction[0][0]}")

if prediction[0][0] >= 0.5:
    print("Class 1")
else:
    print("Class 0")



#Second task
X = np.array([
 [1,2,3,4],
 [2,3,4,5],
 [3,4,5,6],
 [4,5,6,7],
 [5,6,7,8],
 [6,7,8,9],
 [7,8,9,10],
 [8,9,10,11],
 [9,10,11,12],
 [10,11,12,13]
], dtype=float)

y = np.array([0,0,0,0,0,1,1,1,1,1])
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(4,)),
    tf.keras.layers.Dense(
        16,
        activation='relu'
    ),
    tf.keras.layers.Dense(
        8,
        activation = 'relu'
    ),
    tf.keras.layers.Dense(
        1,
        activation = 'sigmoid'
    )
])

model.compile(
    optimizer = 'adam',
    loss = 'binary_crossentropy',
    metrics = ['accuracy']
)

model.summary()

model.fit(
    X,
    y,
    epochs = 200,
    verbose = 1
)

new_data = np.array([[7,8,9,10]])

prediction = model.predict(new_data)

print(f"Prediction probability: {prediction[0][0]}")

if prediction[0][0] >= 0.5:
    print("Class 1")
else:
    print("Class 0")
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from keras.datasets import mnist
from keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(f"x_train의 데이터{x_train.shape}")
print(f"x_test의 데이터{x_test.shape}")
print(x_train.shape[0])
x_train_reshape = x_train.reshape(60000, 784).astype("float32")/255
x_test_reshape = x_test.reshape(10000, 784).astype("float32")/255
y_train_cate = to_categorical(y_train, 10)
y_test_cate = to_categorical(y_test, 10)



model = Sequential()
model.add(Dense(512, input_dim=784, activation = 'relu'))
model.add(Dense(10, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam',  metrics=['acc'])

history=model.fit(x_train_reshape, y_train_cate, epochs=30, batch_size=200, validation_data=(x_test_reshape, y_test_cate))


v_loss= history.history['val_loss']
loss = history.history['loss']
model.save('mnist_ann.h5')

import matplotlib.pyplot as plt

cnt = np.arange(len(v_loss))
plt.plot(cnt, v_loss, marker='.', c='red', label='test')
plt.plot(cnt, loss, marker='.', c='blue', label='train' )
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()
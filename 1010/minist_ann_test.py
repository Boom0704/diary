from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from keras.datasets import mnist
from keras.utils import to_categorical
import matplotlib.pyplot as plt
from keras.models import load_model
from PIL import Image
image = Image.open('./Test2.jpg')
img = image.resize((28, 28)).convert("L")
img = 255 - np.array(img)
plt.imshow(img, 'Grays')
plt.show()

sample = img.reshape(1, 784).astype("float32")/255
model = load_model('./mnist_ann.h5')
model.summary()
pred=model.predict(sample)

print(pred)
pred_cls = np.argmax(pred, 1)
print(pred_cls)
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
#
# sample = x_test[2].reshape(1, 784).astype("float32")/255
# model = load_model('./mnist_ann.h5')
#
# model.summary()
# pred = model.predict(sample)
#
# print(pred)
# pred_cls = np.argmax(pred, 1)
# print(pred_cls)
#
# plt.imshow(x_test[2], 'Greys')

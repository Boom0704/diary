from keras.models import load_model
from keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

sample = x_test[2].reshape(1, 784).astype('float32')/255

model = load_model('./mnist_ann.h5')
model.summary()

pred = model.predict(sample)
import numpy as np
pred_cls = np.argmax(pred, axis=1)
print(pred_cls)
import matplotlib.pyplot as plt
plt.imshow(x_test[2], cmap='Greys')
plt.show()
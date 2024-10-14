from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
image = Image.open('./4.jpg')
# 이미지 크기 변환
img = image.resize((28, 28)).convert("L") # 흑백 28 x 28
img = 255 - np.array(img)
plt.imshow(img, cmap='Greys')
plt.show()
sample = img.reshape(1, 784).astype('float32')/255
model = load_model('./mnist_ann.h5')
model.summary()

pred = model.predict(sample)
print(pred)
pred_cls = np.argmax(pred, axis=1)
print(pred_cls)
plt.show()
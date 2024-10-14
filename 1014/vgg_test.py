from keras.applications import vgg16
from keras.preprocessing.image import load_img, img_to_array
import matplotlib.pyplot as plt
import os

model = vgg16.VGG16()
model.summary()

def fn_predict(p_model, p_file):
    image = load_img(p_file, target_size=(224, 224))
    plt.imshow(image)
    plt.show()
    test_image = img_to_array(image).reshape((1, 224, 224, 3))
    test = vgg16.preprocess_input(test_image)
    pred = p_model.predict(test)
    label = vgg16.decode_predictions(pred)
    pred_cls = label[0][0]
    print(pred_cls[1], pred_cls[2] * 100)

file_list = os.listdir('./imageNet/')
for f in file_list:
    fn_predict(model, './imageNet/' + f)
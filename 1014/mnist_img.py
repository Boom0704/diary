from keras.datasets import mnist
import matplotlib.pyplot as plt
import sys

(x_train, y_train), (x_test, y_test) = mnist.load_data()
plt.imshow(x_train[0], cmap='Greys')
for x in x_train[0]:
    for i in x:
        sys.stdout.write("%d\t" % i)
    sys.stdout.write("\n")
plt.show()
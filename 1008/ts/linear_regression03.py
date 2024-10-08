import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv("./datasets/heights.csv")
x = df['height']
y = df['weight']
# plt.scatter(x,y)
# plt.show()
x = np.array(x.round())
y = np.array(y.round())
# plt.show()

"""
아마도 a = 3 b = 73
"""
a = 0.1
b = 0.1
lr = 0.0001
epochs = 2001

n = len(x)
for i in range(epochs):
    y_pred = a * x + b
    error = y - y_pred
    a_diff = (2 / n) * sum(-x * error)
    b_diff = (2 / n) * sum(-error)
    a = a - lr * a_diff
    b = b - lr * b_diff
    if i % 100 == 0:
        print(f"epoch={i} 기울기 a = {a}  절편 b = {b}")

y_pred = a * x + b
plt.scatter(x, y)

plt.plot([min(x), max(x)], [min(y_pred), max(y_pred)])
plt.show()

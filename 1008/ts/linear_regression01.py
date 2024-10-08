import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 4, 6, 8])
y = np.array([81, 93, 91, 97])
plt.scatter(x, y)
# plt.show()

"""
아마도 a = 3 b = 73
"""
a = 0
b = 0
lr = 0.03
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
plt.plot(x, y_pred, 'r')
plt.show()

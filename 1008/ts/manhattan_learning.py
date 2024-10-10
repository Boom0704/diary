from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from sympy.logic.inference import pl_true

df = pd.read_csv("./datasets/streeteasy/manhattan.csv")
print(df.info())
print(df.columns)

x = df[['bedrooms', 'bathrooms', 'size_sqft',
       'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck',
       'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher',
       'has_patio', 'has_gym']]

y = df[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)
print(x_train.shape, y_train.shape)
print(y_test.shape, y_test.shape)

model = LinearRegression()
model.fit(x_train, y_train)
print(model.coef_)
print(model.intercept_)

y_predicted = model.predict(x_test)
import matplotlib.pyplot as plt
plt.scatter(y_test, y_predicted, alpha=0.5)
plt.xlabel('actual rent')
plt.ylabel('predicted rent')
print("테스트 데이터 정확도 : ", model.score(x_test, y_test))
print("학습 데이터 정확도 : ", model.score(x_train, y_train))
plt.show()

num_samples = 5
random_idx = np.random.choice(x_test.index, size=num_samples, replace =False)
x_sample = x_test.loc[random_idx]
y_sample_actual = y_test.loc[random_idx]

y_sample_pred = model.predict(x_sample)
for i in range(num_samples):
    print(f"샘풀 {i+1}")
    print(f"실제 임대료 : {y_sample_actual.iloc[i].values[0]}")
    print(f"에측 임대료 : {y_sample_pred[i]}")


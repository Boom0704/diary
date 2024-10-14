#pip install scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
from sympy.core.random import random

df = pd.read_csv("./datasets/streeteasy/manhattan.csv")
print(df.info)
print(df.columns)

x = df[['bedrooms', 'bathrooms', 'size_sqft',
       'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck',
       'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher',
       'has_patio', 'has_gym']]
y = df[['rent']]
print(x.head())
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)  # 8:2 로 트레이닝, 테스트 나눔
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)
model = LinearRegression()
model.fit(x_train, y_train)
print(model.coef_)       # 기울기
print(model.intercept_)  # y절편
# 테스트 데이터로 예측
y_predicted = model.predict(x_test)
import matplotlib.pyplot as plt
plt.scatter(y_test, y_predicted, alpha=0.4)
plt.xlabel('actual rent')
plt.ylabel('predicted rent')
print("테스트 데이터 정확도:", model.score(x_test, y_test))
print("학습 데이터 정확도:", model.score(x_train, y_train))
plt.show()
import numpy as np
# x_test 에서 임의로 5개 샘플 선택
num_samples =  5
random_inx = np.random.choice(x_test.index, size=num_samples, replace=False)
x_sample = x_test.loc[random_inx]
y_sample_actual = y_test.loc[random_inx]

# 선택한 샘플로 예측
y_sample_pred = model.predict(x_sample)
for i in range(num_samples):
    print(f"샘플 {i + 1}")
    print(f"실제 임대료: {y_sample_actual.iloc[i].values[0]}")
    print(f"예측 임대료: {y_sample_pred[i]}" )
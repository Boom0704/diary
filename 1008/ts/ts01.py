from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv('./datasets/streeteasy/manhattan.csv')

print(df.info())
print(df.columns)

# 독립 변수(X)와 종속 변수(y) 설정
X = df[['bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee',
        'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher',
        'has_patio', 'has_gym']]

y = df['rent']  # 종속 변수는 월세 가격

# 데이터셋을 훈련/테스트 세트로 분할 (train_size=0.8)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 선형 회귀 모델 생성 및 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 테스트 세트로 예측
y_pred = model.predict(X_test)

# 모델 평가 (결정 계수 R^2)
test_score = model.score(X_test, y_test)
train_score = model.score(X_train, y_train)

# 정확도를 소수점 2자리까지 출력
print(f"Test Data R^2 Score: {test_score:.2%}")
print(f"Train Data R^2 Score: {train_score:.2%}")

# 실제 값과 예측 값 비교
results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(results.head())

# 결과 시각화 (산점도)
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred, color='blue', alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2)
plt.title('Actual vs Predicted Rent Prices')
plt.xlabel('Actual Rent')
plt.ylabel('Predicted Rent')
plt.show()

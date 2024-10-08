import matplotlib.pyplot as plt
import numpy as np

# 데이터 정의
x = np.array([2, 4, 6, 8])  # 공부 시간 (독립 변수)
y = np.array([81, 93, 91, 97])  # 시험 점수 (종속 변수)

# 그래프 크기 설정
plt.figure(figsize=(8, 5))

# 산점도 그리기 (공부 시간과 시험 점수의 관계를 시각화)
plt.scatter(x, y)

# 선형 회귀 모델의 초기 변수 설정
a = 0  # 기울기 (처음에는 0으로 설정)
b = 0  # 절편 (처음에는 0으로 설정)

# 학습률 설정 (learning rate)
# 학습률은 각 반복 시 기울기와 절편을 얼마나 업데이트할지를 결정함
lr = 0.03

# 반복할 횟수 (epochs)
# 경사 하강법을 몇 번 실행할 것인지 설정
epochs = 2001

# 데이터 포인트의 개수 (x의 데이터 개수)
n = len(x)

# 경사 하강법 반복
# 경사 하강법을 통해 a와 b를 업데이트하며 최적의 값을 찾아가는 과정
for i in range(epochs):
    # y_pred는 현재 기울기 a와 절편 b로 예측한 y 값
    y_pred = a * x + b
    
    # 예측값과 실제 값의 차이를 오차로 정의 (y - y_pred)
    error = y - y_pred
    
    # a에 대한 기울기 (경사) 계산
    # x와 오차(error)를 곱한 값의 평균에 음수를 곱함 (기울기를 줄이기 위한 값)
    a_diff = -(2/n) * sum(x * error)
    
    # b에 대한 기울기 (경사) 계산
    # 오차(error)의 평균에 음수를 곱함 (절편을 줄이기 위한 값)
    b_diff = -(2/n) * sum(error)
    
    # 기울기 a를 업데이트 (a - 학습률 * 기울기의 변화량)
    a = a - lr * a_diff
    
    # 절편 b를 업데이트 (b - 학습률 * 절편의 변화량)
    b = b - lr * b_diff

    # 100번마다 기울기와 절편, 오차 값을 출력
    if i % 100 == 0:
        print(f'epoch: {i}, a: {a}, b: {b}, error: {error}')

# 최종적으로 학습된 a와 b 값을 사용하여 예측값을 계산
y_pred = a * x + b

# 산점도에 학습된 선형 회귀선을 추가
plt.scatter(x, y)  # 실제 데이터 산점도
plt.plot(x, y_pred, color='red')  # 예측된 회귀선 (빨간색으로 표시)
plt.title('Linear Regression')  # 그래프 제목
plt.xlabel('Study Hours')  # x축 라벨: 공부 시간
plt.ylabel('Score')  # y축 라벨: 시험 점수
plt.show()  # 그래프 출력

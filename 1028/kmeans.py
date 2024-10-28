import pandas as pd
from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 데이터 로드
iris = datasets.load_iris()
label = pd.DataFrame(iris.target)
label.columns = ['labels']
data = pd.DataFrame(iris.data)

# 컬럼 이름 설정
data.columns = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width']
data = pd.concat([data, label], axis=1)

# 데이터 출력
print(data.head())

# KMeans 모델 생성 및 학습
model = KMeans(n_clusters=3)
x_data = data[['Petal length', 'Petal width']]
# x_data = data[['Sepal length', 'Sepal width']]
model.fit(x_data)
pred = pd.DataFrame(model.predict(x_data), columns=['predict'])
all_data = pd.concat([data, pred], axis=1)

# 산점도 그리기
plt.scatter(all_data['Petal length'], all_data['Petal width'], c=all_data['predict'], alpha=0.5)
# plt.scatter(all_data['Sepal length'], all_data['Sepal width'], c=all_data['predict'], alpha=0.5)

# 클러스터 중심 좌표
center = pd.DataFrame(model.cluster_centers_, columns=['Petal length', 'Petal width'])
# center = pd.DataFrame(model.cluster_centers_, columns=['Sepal length', 'Sepal width'])
plt.scatter(center['Petal length'], center['Petal width'], s=50, marker='D', c='r')

# 그래프 보여주기
plt.show()

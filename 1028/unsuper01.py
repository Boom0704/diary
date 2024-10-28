import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 데이터 로드
df = pd.read_csv('../ex_unsuper/data/Mall_Customers.csv')

# 성별을 숫자로 변환
df['Gender'] = df['Gender'].map({'Female': 1, 'Male': 0})

print(df.columns)
data = df[['Gender', 'Age', 'Annual Income', 'Spending Score']]

# 데이터 정보 출력
print(data.info())
print(data.describe())

# KMeans 모델을 위한 inertia 값 계산
inertia = []
for i in range(1, 11):
    model = KMeans(n_clusters=i)
    model.fit(data)
    inertia.append(model.inertia_)

# 클러스터 개수에 따른 inertia 값 시각화
plt.plot(range(1, 11), inertia, 'o-')
plt.xlabel('Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()

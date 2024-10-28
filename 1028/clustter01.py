import pandas as pd
from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
df = pd.read_csv('../ex_unsuper/data/Mall_Customers.csv')
df['Gender'] = df['Gender'].map({'Female':1, 'Male':0})
print(df.columns)
data = df[['Gender', 'Age', 'Annual Income', 'Spending Score']]
print(data.info())
pring(data.describe())

inertia = []
for i in range(1,11):
    model = KMeans(n_clusters=i)
    model.fit(data)
    inertia.append(model.inertia_)
plt.plot(len(inertia), inertia, '-0')
plt.xlabel('cludtaer(k)')
plt.ylabel('inertia')
plt.show()
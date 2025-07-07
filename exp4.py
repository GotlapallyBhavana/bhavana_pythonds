import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data={
    'name':["a","b","c","d","e"],
    'age':[24,35,26,45,29],
    'dept':["IT","CSE","IOT","CSE","IT"],
    'salary':[15000,26000,45000,26000,35000],
    'joindate':pd.to_datetime(['2022-06-01','2021-08-05','2025-06-01','2021-08-05','2023-06-01'])
    }
df=pd.DataFrame(data)
# labels=df['name'].tolist()
# ages=df['age'].tolist()
# plt.bar(labels,ages,color="green")
# plt.show()

# sns.barplot(x='name',y='age',data=df)
# plt.show()
# sns.barplot(x='dept',y='salary',data=df,estimator=sum)
# plt.show()
# sns.countplot(x='dept',data=df)
# plt.show()


fig,axs=plt.subplots(1,3,figsize=(12,5))
sns.barplot(x='dept',y='salary',data=df,estimator=sum,ax=axs[0])
sns.countplot(x='dept',data=df,ax=axs[1])
sns.histplot(df['age'],kde=True,ax=axs[2])
plt.tight_layout()
plt.show()
import pandas as pd
data={
'name':["a","b","c","d","e"],
'age':[24,35,26,45,29],
'dept':["IT","CSE","IOT","CSE","IT"],
'salary':[15000,26000,45000,26000,35000],
'joindate':pd.to_datetime(['2022-06-01','2021-08-05','2025-06-01','2021-08-05','2023-06-01'])
}
# print(data)
df=pd.DataFrame(data)
print(df)
# print(df.head(1))
# print(df.shape)
# print(df.dtypes)
# arr=df.columns.tolist()
# print(arr)
# print(df[['name','dept']])
# print(df[df['dept']=="IT"])
# print(df[df['salary']>20000])
# print(df[(df['dept']=="CSE") & (df['salary']>25000)])
# print(df.groupby('dept')['salary'].sum())
print(df['dept'].value_counts())
df['bonus']=df['salary']*0.10
print(df)
df['joiningyear']=df['joindate'].dt.year
print(df)
# df.rename(columns={'joindate':'joiningdate'},inplace=True)
# print(df)
# df.drop(columns=['joiningyear'],inplace=True)
# print(df)
# df=df.sort_values(by='salary',ascending=True)
# print(df)
print(df.loc[df.groupby('dept')['salary'].idxmax()])
print(df)
df['seniority']=df['age'].apply(lambda x: 'senior' if x>30 else 'junior' )
print(df)

df.to_csv("employee.csv",index=False)
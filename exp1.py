import numpy as np
# arr=np.arange(10)
# arr1=np.arange(10,50,5)
# arr2=np.arange(50,10,-5)
# print(arr)
# print(arr1)
# # print(arr2)
# n=3
# for i in range(n):
#     odd=2*i+1
#     print(odd*(odd+1),odd+1,odd)
# col3=np.arange(1,2*n,2)
# col2=np.arange(2,2*n+1,2)
# col1=col2*col3
# print(col1,col2,col3)
# res=np.column_stack((col1,col2,col3))
# print(res)
# list1=[10,80,60,40,20,90]
# arr=np.array(list1)
# print(arr)
# op=[1]*len(list1)
# print(op)
# op1=np.ones_like(arr)
# print(op1)
# matrix=np.ones((3,3))
# print(matrix)
# mat1=np.random.randint(10,50,size=(3,4))
# print(mat1)
# otp=np.random.randint(100000,999999)
# print(otp)

# list1=[10,80,60,40,20,90]
# arr=np.array(list1)
# print(np.max(arr))
# print(np.mean(arr))
# print(np.sum(arr))

arr=np.arange(10)
arr[arr%2==0]*2
print(arr)
arr1=np.array([1,5,-6,-4,6,7])
arr1[arr1<0]=0
print(arr1)

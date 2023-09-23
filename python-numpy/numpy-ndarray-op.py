#載入numpy套件
import numpy as np

#逐元運算(elementwise):對每個資料逐一運算
#data1=np.array([3,2,10])
#data2=np.array([1,3,6])
#result=data1+data2
#print("加法",result)
#result=data1*data2
#print("乘法",result)
#result=data1>data2
#print("大於",result)
#result=data1==data2
#print("是否相等",result)


#矩陣運算(matrix):對兩個矩陣進行矩陣運算
#data1=np.array([
#    [1,3]
#])  #1x2
#data2=np.array([
#    [2,-1,3],
#    [-2,4,1]
#])  #2x3
#result=data1@data2  
#print("內積",result)  #得到1x3的矩陣
#result=np.outer(data1,data2)
#print("外積",result)  #得到2x6的矩陣


#統計運算(statistics):對單一陣列進行統計運算
data=np.array([
    [2,1,7],
    [-5,3,8]
])  #2x3
#result=data.sum()
#print("總和",result)
#result=data.max()
#print("最大值",result)
#result=data.mean()
#print("平均數",result)
#result=data.std()
#print("標準差",result)

#result=data.sum(axis=0)  #針對欄column(第一個維度)做總合
#print(result)
#result=data.sum(axis=1)  #針對列row(第二個維度)做總合
#print(result)
#result=data.max(axis=0)  
#print(result)
#result=data.mean(axis=1)  
#print(result)

result=data.cumsum()  #逐值累加
print(result)
result=data.cumsum(axis=0)  #針對欄做逐值累加(第一個維度)
print(result)
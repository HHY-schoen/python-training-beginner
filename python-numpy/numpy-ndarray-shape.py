#載入numpy套件
import numpy as np

#多維陣列維度/形狀操作
#觀察資料形狀
#data=np.ones(10)
#print(data.shape)
#data=np.array([
#    [3,1,5],
#    [1,2,3]
#    ])
#print(data.shape)

#資料轉置
#data=np.array([
#    [2,4,1],
#    [1,5,0]
#    ])
#print(data.shape)  #(2,3)
#print(data.T.shape)  #(3,2)

#扁平化資料
#data=np.array([
#    [
#         [2,1,3],[1,2,3]
#    ],
#    [
#         [0,2,1],[8,9,10]
#    ]
#    ])  #(2,2,3)
#newData=data.ravel()  
#print(newData)
#print(newData.shape)  #(12,)

#重塑資料形狀
#data=np.array([
#    [
#         [2,1,3],[1,2,3]
#    ],
#    [
#         [0,2,1],[8,9,10]
#    ]
#    ])  #2x2x3=12
#newData=data.reshape(1,2,6)  #1x2x6=12
#print(newData)
##newData=data.reshape(3,5)  #3x5=15> 錯誤
#print(newData.shape)  #(1,2,6)

#初始化資料
data=np.zeros(18).reshape(3,2,3)
print(data)

data=np.arange(9).reshape(3,3)
print(data)
print(data.T)


#維度:資料的層次
#形狀shape:同時表達資料的層次，和每個層次的資料數量
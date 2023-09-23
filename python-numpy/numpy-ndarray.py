#載入numpy套件
import numpy as np
#建立一維陣列
#data=np.array([3,2,6,4])
#print(data)
#data=np.empty(4)  #創造一個有四個資料的一維陣列，資料未指定
#print(data)
#data=np.zeros(3)  #創造三個資料都是0的一維陣列(浮點數)
#print(data)
#data=np.ones(3)  #創造三個資料都是1的一維陣列
#print(data)
#data=np.arange(5)  #創造五個資料連續的一維陣列
#print(data)

#建立二維陣列
#data=np.array([  #創造一個3x3的二維陣列
#    [2,3,2],
#    [1,5,2],
#    [4,2,1]
#])
#print(data)
#data=np.empty([3,3])  #創造一個3x3的二維陣列，資料未指定
#print(data)
#data=np.ones([2,3])  #創造一個2x3的二維陣列，資料都是1
#print(data)

#建立三維陣列
#data=np.array([  #根據列表創造一個2x2x2的三維陣列
#    [
#         [3,1],[1,2]
#    ],
#    [
#         [2,5],[10,2]
#    ]
#       ])
#print(data)
#data=np.zeros([3,1,3])  #創造一個3x1x3的三維陣列，資料都是0
#print(data)

#建立高維陣列
#data=np.array([  #創造一個1x1x2x3的四維陣列
#    [
#         [
#             [3,2,1],
#             [5,5,10]
#         ]
#    ]
#       ])
#print(data)
data=np.ones([2,1,1,2])  #創造一個2x1x1x2的四維陣列，資料都是1
print(data)


#ndarray多維陣列(N-Dimensional Array)
#多維陣列ndarray是NumPy的核心物件

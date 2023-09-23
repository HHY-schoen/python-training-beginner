#載入pandas模組
import pandas as pd
#建立Series
#data=pd.Series([20,10,15])
#基本Series操作
#print(data)
#print("Max:",data.max())
#print("Median:",data.median())
#data=data*2
#data=data==20
#print(data)


#建立DataFrame
data=pd.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":[30000,50000,40000]
    })
#基本Dataframe操作
print(data)
#print(data["salary"])  #取得特定的欄位
print("----")
print(data.iloc[1])  #取得特定的列


#Pandas:概念類似試算表的資料分析套件
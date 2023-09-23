import pandas as pd
#讀取資料
data=pd.read_csv("googleplaystore.csv")  #把csv格式的檔案讀取成一個DataFrame
#觀察資料
print("資料數量",data.shape)
print("資料欄位",data.columns)
print("==========================")

#分析資料:評分各種統計數據
#condition=data["Rating"]<=5
#data=data[condition]
#print("平均數",data["Rating"].mean())
#print("中位數",data["Rating"].median())
#print("前一千個應用程式的平均",data["Rating"].nlargest(1000).mean())

#分析資料:安裝數量的各種統計數據
#data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))
#print(data["Installs"])
#print("平均數",data["Installs"].mean())
#condition=data["Installs"]>100000
#print("安裝數量大於十萬的應用程式有幾個",data[condition].shape[0])

#基於資料的應用:關鍵字搜尋應用程式名稱
keyword=input("請輸入關鍵字:")
condition=data["App"].str.contains(keyword,case=False)  #case=False:忽略大小寫
#print(data[condition]["App"])  #包含關鍵字程式的名稱
print("包含關鍵字程式的數量",data[condition].shape[0])  #shape[0]:清除欄位總數的資料



#資料工程:收集資料> 清理資料> 分析資料> 基於資料的應用
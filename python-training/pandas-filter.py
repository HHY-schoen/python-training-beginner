#載入pandas模組
import pandas as pd
#篩選練習-Series
#data=pd.Series([30,15,620])
#condition=data>18
#print(condition)  #會印出布林值
#filteredData=data[condition]
#print(filteredData)

#data=pd.Series(["您好","Python","Pandas"])
#condition=data.str.contains("P")
#print(condition)
#filteredData=data[condition]
#print(filteredData)

#篩選練習-DataFrame
data=pd.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[30000,50000,40000]
    })
#print(data)
condition=data["name"]=="Amy"
print(condition)
filteredData=data[condition]
print(filteredData)
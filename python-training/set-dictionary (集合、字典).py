#集合的運算
#s1={3,4,5}
#print(3 not in s1)
#s1={3,4,5}
#s2={4,5,6,7}
#s3=s1&s2  #交集:取兩個集合中相同的資料
#s3=s1|s2  #聯集:取兩個集合中的所有資料，但不重複取
#s3=s1-s2  #差集:從s1中，減去和s2重疊的部分
#s3=s1^s2  #反交集:取兩個集合中，不重疊的部分
#print(s3)
#s=set("Hello")  #把字串中的字母拆解成集合:set(字串)
#print("H" in s)

#字典的運算:key-value配對
#dic={"apple":"蘋果","bug":"蟲蟲"}
#dic["apple"]="小蘋果"
#print(dic["apple"])
#print("apple" in dic)  #判斷key是否存在
#del dic["apple"]  #刪除字典中的鍵值對(key-value pair)
dic={x:x*2 for x in [3,4,5]}  #從列表的資料產生字典
print(dic)

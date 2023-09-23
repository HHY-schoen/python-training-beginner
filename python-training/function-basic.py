#定義函式
#函式內部的程式碼，若沒有做函式呼叫，就不會執行
#def multiply(n1,n2):
    #print(n1*n2)
#    return n1*n2  #若沒特別定義，則回傳None
#return的好處:可在外部繼續進行操作


#呼叫函式
#multiply(3,4)
#multiply(10,8)
#value=multiply(3,4)+multiply(10,5)
#print(value)


#函式可用來做程式的包裝:同樣的邏輯可以重複利用
def calculate(max):
    sum=0
    for n in range(1,max+1):
        sum=sum+n
    print(sum)
    
calculate(10)
calculate(20)

#參數:讓函式更有彈性
#函式最大的優點:程式的包裝
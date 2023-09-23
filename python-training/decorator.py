#定義裝飾器
#def myDeco(cb):
#    def run():
#        print("裝飾器中的程式碼")
#        cb(5)  #此回呼函式，其實就是被裝飾器的普通函式
#    return run

#使用裝飾器
#@myDeco
#def test(n):
#    print("普通函式的程式碼",n)

#test()


#定義一個裝飾器，計算1+2+...+50的總和
def calculate(callback):
    def run():
        #裝飾器要執行的程式碼
        result=0
        for n in range(51):
            result+=n
        #把計算結果透過參數傳到被裝飾器的普通函式中
        callback(result)
    return run

#使用裝飾器
@calculate
def show(n):
    print("計算結果是",n)
    
@calculate
def showEnglish(n):
    print("Result is",n)
   
show()
showEnglish()


#裝飾器Decorator:特殊函式，用來「輔助」其他函式
#先執行裝飾器程式碼，再執行下面的程式碼
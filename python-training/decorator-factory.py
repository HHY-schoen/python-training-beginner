#def myFactory(base):
#    def myDeco(cb):
#        def run():
#            print("裝飾器內的程式",base)
#            result=base*2
#            cb(result)
#        return run
#    return myDeco

#@myFactory(5)  #裝飾器工廠後需家小括號
#def test(result):
#    print("普通函式的程式碼",result)

#test()


#計算1+2+...+50的裝飾器
def calculateFactory(max):
    def calculate(callback):
        def run():
            total=0
            for n in range(max+1):
                total+=n
            callback(total)
        return run
    return calculate
         
@calculateFactory(100)
def show(result):
    print("結果是",result)
@calculateFactory(10)
def showEnglish(result):
    print("Result is",result)
    
show()
showEnglish()


#裝飾器工廠Decorate Factory:用來「生產」裝飾器的函式
#裝飾器工廠可另外接收額外參數、更彈性
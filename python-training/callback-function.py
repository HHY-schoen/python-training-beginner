#def test(arg):
#    arg("Hello")  #呼叫回呼函式，帶入參數

#定義一個回呼函式
#def handle(da):
#    print(da)   

#test(handle)


def add(n1,n2,cb):
    cb(n1+n2)

def handle1(result):
    print("結果是",result)

def handle2(result):
    print("Result of Add is",result)

add(3,4,handle1)
add(5,6,handle1)
add(4,2,handle2)

#回呼函式callback:透過參數傳遞函式到另一個函式中

#建立生成器函式
#def test():
#    print("階段一")
#    yield 5
#    print("階段二")
#    yield 10

#呼叫並回傳生成器
#gen=test()  #將生成器放入變數gen
#print(gen)  

#搭配for迴圈中使用
#for d in gen:
#    print(d)

def generateEven(maxNumber):
    number=0
    while number<=maxNumber:
        yield number
        number+=2
evenGenerator=generateEven(16)
for data in evenGenerator:
    print(data)



#生成器Generator:動態產生可疊代資料，搭配for迴圈使用
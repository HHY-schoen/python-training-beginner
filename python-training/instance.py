#Point實體物件的設計:平面座標上的點
#class Point:
#    def __init__(self,x,y):
#        self.x=x
#        self.y=y
#p1=Point(3,4)  #建立第一個實體物件
#print(p1.x,p1.y)
#p2=Point(5,6)  #建立第二個實體物件
#print(p2.x,p2.y)


#Fullname實體物件的設計:分開紀錄姓、名的資料全名
class Fullname:
    def __init__(self,first,last):
        self.first=first
        self.last=last
name1=Fullname("C.W","Peng")
print(name1.first,name1.last)
name2=Fullname("T.Y","Lin")
print(name2.first,name2.last)
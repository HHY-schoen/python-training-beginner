from flask import Flask 
app=Flask(__name__)  #__name__代表目前執行的模組

@app.route("/")  #函式的裝飾(Decorator):以函式為基礎，提供附加的功能
def home():
    return "Hello Flask 2"

@app.route("/text")  #代表我們要處理的網站路徑
def test():
    return "This is test"


if __name__=="__main__":  #如果以主程式執行
    app.run()  #立刻啟動伺服器        
    
    
#Flask:架設網站的套件
#實際網站程式必須24小時運行，不可中斷

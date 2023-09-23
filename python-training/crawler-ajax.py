# 抓取Medium.com的文章資料
import urllib.request as req
url="https://medium.com/_/graphql"

# 建立一個Request物件，附加Request Headers的資訊
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")  #跟據觀察，取得的資料是JSON格式


# 解析JSON格式資料，取得每篇文章的標題
import json
data=data.replace("])}while(1);</x>"," ")  #換成空字串
data=json.loads(data)  #把原始的JSON資料解析成字典/列表的表示形式

# 取得JSON資料中的文章標題
posts=data["payload"]["referances"]["Post"]
for key in posts:
    post=posts[key]
    print(post["title"])


# AJAX:網頁前端的JavaScript程式技術
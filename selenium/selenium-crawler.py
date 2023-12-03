from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

#設定chromedriver的執行檔路徑
options = Options()
options.chrome_executable_path='C:/Users/User/Downloads/chromedriver-win64/chromedriver.exe'
#r建立driver實體物件，用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)

#連線至網頁
driver.get('https://www.ptt.cc/bbs/Stock/index.html')
titles = driver.find_elements(By.CLASS_NAME, "title")
for title in titles:
    print(title.text)

#取得上一頁的文章標題
link = driver.find_element(By.LINK_TEXT, "‹ 上頁")
link.click()
titles = driver.find_elements(By.CLASS_NAME, "title")
for title in titles:
    print(title.text)

#螢幕截圖
driver.maxmize_window()  #視窗最大化
driver.save_screenshot('test1.jpg')

# driver.get('https://www.dcard.tw/f')
# search = driver.find_element('name','query')  #找到搜尋欄位
# search.send_keys('比特幣')
# search.send_keys(Keys.RETURN)  #壓ENTER送出

time.sleep(3)
driver.close()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.chrome_executable_path = 'C:/Users/User/Downloads/chromedriver-win64/chromedriver.exe'

driver = webdriver.Chrome(options=options)

#連線到登入頁面，輸入帳密
driver.get('https://leetcode.com/accounts/login/')
username = driver.find_element(By.ID, 'id_login')
password = driver.find_element(By.ID, 'id_password')
username.send_keys('帳號')
password.send_keys('密碼')
signinBtn = driver.find_element(By.ID, 'signin_btn')
signinBtn.send_keys(Keys.RETURN)
#等待登入完成
time.sleep(5)
#連線到我們想要的網址
driver.get('https://leetcode.com/problemset/all/')
time.sleep(3)
element = driver.find_element(By.CSS_SELECTOR, "[data-difficulty=TOTAL]")
# print(element.text)
column = element.text.split('\n')  #把字串根據換行符號做切割
print('已完成刷題數量:',column[1])

driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.chrome_executable_path='C:/Users/User/Downloads/chromedriver-win64/chromedriver.exe'

driver = webdriver.Chrome(options=options)
driver.get('https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0')

#捲動視窗，並等待瀏覽器載入更多內容
n = 0
while n < 3:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')  #捲動到視窗底部
    time.sleep(3)
    n += 1

titles = driver.find_elements(By.CLASS_NAME, 'base-search-card__title')
for title in titles:
    print(title.text)

driver.close()
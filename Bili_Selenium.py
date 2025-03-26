from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

path = Service('C:\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service = path)
driver.maximize_window()

driver.get('https://www.bilibili.com/v/popular/all/?spm_id_from=333.1007.0.0')

search_avatar = driver.find_elements(By.CLASS_NAME, 'video-name')
#将发出请求时生成的静态页面以图片的形式保存在程序同个目录下
driver.get_screenshot_as_file('screenshot.png')

for a in search_avatar:
    print(a.text)
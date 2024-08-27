from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


Wd = webdriver.Chrome()
Wd.get('https://www.bilibili.com')
element_search_input = Wd.find_element(By.CLASS_NAME, 'nav-search-input' )
element_search_input.send_keys('紫罗兰花园')

time.sleep(3)

element_search_confirm = Wd.find_element(By.CSS_SELECTOR, 'svg[width="17"][height="17"]')
element_search_confirm.click()

input()
Wd.quit()

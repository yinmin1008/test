from selenium import webdriver
import time
from tools import is_exist,find_element

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('http://132.232.44.158:9999/shopxo/')

bao = ('xpath','//*[@id="floor1"]/div[2]/div[2]/div[1]/a/img')
find_element(driver,bao).click()

# 切换到最后一个网页
driver.switch_to_window(driver.window_handles[-1])

buy =("xpath",'/html/body/div[4]/div[2]/div[2]/div[3]/div[2]/div/button')
find_element(driver,buy).click()

# driver.quit()

# 0，导入selenium
# 1,打开浏览器
# 2，打开网址
# 3，执行用例
# 4，断言结果

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get('https://www.taobao.com/')

driver.find_element_by_id('q').send_keys('相机')
driver.find_element_by_class_name('search-button').click()
time.sleep(3)
assert driver.title == '淘宝网 - 淘！我喜欢'


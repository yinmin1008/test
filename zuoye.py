from selenium import webdriver
import time
from tools import is_exist,find_element




driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('http://132.232.44.158:9999/shopxo/admin.php')
driver.maximize_window()

# driver.find_element_by_name('username').send_keys('admin')
# driver.find_element_by_name('login_pwd').send_keys('shopxo')
# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[3]/button').click()
# time.sleep(3)
# e = is_element_exist(driver,'xpath','//*[@id="admin-offcanvas"]/div/ul/li[1]/a/span[2]')

# assert e is True
# print("测试通过")

username =('name','username')
password =('name','login_pwd')
login =('xpath','/html/body/div[1]/div/div[2]/div/form/div/div[3]/button')

find_element(driver,username).send_keys('admin')
find_element(driver,password).send_keys('shopxo')
find_element(driver,login).click()
index = ('xpath','//*[@id="admin-offcanvas"]/div/ul/li[1]/a/span[2]')
print(find_element(driver,index).text)
assert is_exist(driver,index) is True
print('测试用例通过')
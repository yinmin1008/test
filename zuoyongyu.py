from selenium import webdriver
import time
from tools import is_exist,find_element

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('http://132.232.44.158:9999/shopxo/admin.php')
# driver.maximize_window()
username =('name','username')
password =('name','login_pwd')
login =('xpath','/html/body/div[1]/div/div[2]/div/form/div/div[3]/button')

find_element(driver,username).send_keys('admin')
find_element(driver,password).send_keys('shopxo')
find_element(driver,login).click()

# 切换至小窗口/作用域
iframe = ('id','ifcontent')
e = find_element(driver,iframe)
driver.switch_to_frame(e)
count = ('xpath','/html/body/div[1]/div/div[1]/div/span[2]') 
print(find_element(driver,count).text)
try:
    assert find_element(driver,count).text == '商城统计'
    print('测试用例通过')
except:
    print('测试用例失败')

# 切回大网页
driver.switch_to_default_content()

index = ('xpath','//*[@id="admin-offcanvas"]/div/ul/li[1]/a/span[2]')
print(find_element(driver,index).text)
assert is_exist(driver,index) is True
print('测试用例通过')
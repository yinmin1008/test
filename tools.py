from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def find_element(driver,locator):
    '''
    查找元素
    local:定位元素的方式和值
          id=（'id':'    '）
    '''
    return WebDriverWait(driver, 30).until(lambda s: s.find_element(*locator))


def is_exist(driver,locator):
    try:
        find_element(driver,locator)
        return True
    except:
        return False


def is_element_exist(driver,by,val):
    '''
    判断元素是否存在
    存在返回true
    不存在返回false
    '''
    try:
        if by == 'id':
            driver.find_element_by_id(val)
        if by == 'xpath':
            driver.find_element_by_xpath(val)
        return True
    except:
        return False


  
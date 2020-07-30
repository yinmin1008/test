from selenium.webdriver.support.ui import WebDriverWait

def find_element(driver, locator):
    """
        方法：动态查找元素，显式等待
        参数：
            - driver：浏览器的句柄
            - locator：元素的定位方式和值
                id = ('id', 'xxx')
                name = ('name', 'xxxx')
                xpath = ('xpath', 'xxx')
                tag_name = ('tag name', 'xxx'')
                link_text = ('link text', 'xxx')
                class_name = ('class name', 'xxx')
                css_selector = ('css selector', 'xxx')
                partial_link_text = ('partial link text', 'xxx')
        返回:返回元素
    """
    return WebDriverWait(driver, 30).until(lambda s: s.find_element(*locator))


def is_elemenet_exist(driver, locator):
    """
        方法：判断元素是否存在
        参数：
            - driver：浏览器的句柄
            - locator：元素的定位方式和值
                id = ('id', 'xxx')
                name = ('name', 'xxxx')
                xpath = ('xpath', 'xxx')
                tag_name = ('tag name', 'xxx'')
                link_text = ('link text', 'xxx')
                class_name = ('class name', 'xxx')
                css_selector = ('css selector', 'xxx')
                partial_link_text = ('partial link text', 'xxx')
        返回：
            True：元素存在
            False：元素不存在
    """
    try:
        find_element(driver, locator)
        return True
    except:
        return False



def is_elemenet_exist_old(driver, by, val):
    """
        方法：判断元素是否存在
        参数：
            - by：元素定位的方式
            - val：定位方式的值
        返回：
            True：元素存在
            False：元素不存在
    """
    try:
        if by == "id":
            driver.find_element_by_id(val)
        if by == "xpath":
            driver.find_element_by_xpath(val)
        return True
    except:
        return False



from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, browserType):
        """
        传入browserType,确定初始化浏览器类型
        :param browserType:
        """
        if browserType == 'Chrome':
            self.driver = webdriver.Chrome()
        elif browserType == 'Firefox':
            self.driver = webdriver.Firefox()
        elif browserType == 'Ie':
            self.driver = webdriver.Ie()
        else:
            print('浏览器类型输入错误')

    def maxwindow(self):
        """
        窗口最大化
        :return:
        """
        self.driver.maximize_window()

    def get_url(self, url):
        """
        打开网页
        :return:
        """
        self.driver.get(url)



    def get_by_param(self, elemtarget):
        """
        将传入的"i,su",转换为BY类定位的参数：(BY.id, su)
        :param elempath:
        :return:
        """
        slelct_by = elemtarget.split(',')[0].strip()
        slelct_valve = elemtarget.split(',')[1].strip()

        if slelct_by == 'i' or slelct_by == 'id':
            by_param = (By.ID, slelct_valve)
        elif slelct_by == 'n' or slelct_by == 'name':
            by_param = (By.NAME, slelct_valve)
        elif slelct_by == 'c' or slelct_by == 'class':
            by_param = (By.CLASS_NAME, slelct_valve)
        elif slelct_by == 'x' or slelct_by == 'xpath':
            by_param = (By.XPATH, slelct_valve)
        elif slelct_by == 'tag' or slelct_by == 'tag_name':
            by_param = (By.TAG_NAME, slelct_valve)
        elif slelct_by == 'link' or slelct_by == 'link_text':
            by_param = (By.LINK_TEXT, slelct_valve)
        elif slelct_by == 'partial' or slelct_by == 'partial_link_text':
            by_param = (By.PARTIAL_LINK_TEXT, slelct_valve)
        elif slelct_by == 'css' or slelct_by == 'css_selector':
            by_param = (By.CSS_SELECTOR, slelct_valve)
        else:
            print('定位文本传入格式错误，例如"i,su"')
        return by_param

    def webwait(self, elemtarget):
        WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self.get_by_param(elemtarget)))

    def get_element(self, elemtarget):
        """
        定位到到单个元素
        :return:
        """
        self.webwait(elemtarget)
        return self.driver.find_element(*self.get_by_param(elemtarget))

    def get_elements(self, elemtarget, indx=0):
        """
        通过下标定位到复数元素中的某个目标
        :param elemtarget:
        :param indx:
        :return:
        """
        self.webwait(elemtarget)
        return self.driver.find_elements(*self.get_by_param(elemtarget))[indx]

    def element_click(self, elemtarget):
        """
        点击定位到单个目标元素
        :return:
        """
        self.get_element(elemtarget).click()

    def element_sendkeys(self, elemtarget, value):
        """
        输入文本
        :param elemtarget:
        :param value:
        :return:
        """
        self.get_element(elemtarget).clear()
        self.get_element(elemtarget).send_keys(value)

    def elements_click(self, elemtarget, indx=0):
        """
        对定位到的元素组中的某个元素进行点击
        :param elemtarget:
        :param indx:
        :return:
        """
        self.get_elements(elemtarget, indx).click()

    def elements_sendkeys(self, elemtarget, value, indx=0):
        """
        对定位到的元素组中的某个元素进行文本输入
        :param elemtarget:
        :param indx:
        :return:
        """
        self.get_elements(elemtarget, indx).clear()
        self.get_elements(elemtarget, indx).send_keys(value)

    def switch_to_iframe(self, elemtarget):
        """
        定位到iframe框架
        :return:
        """
        self.driver.switch_to.frame(self.get_element(elemtarget))

    def select_by_indx(self, elemtarget, selectindx=0):
        """
        根据选择框的下标索引进行选择
        :param elemtarget:
        :param selectindx:
        :return:
        """
        Select(self.get_element(elemtarget)).select_by_index(selectindx)

    def select_by_text(self, elemtarget, text):
        """
        根据选择框中的文本进行选择
        :param elemtarget:
        :param text:
        :return:
        """
        Select(self.get_element(elemtarget)).select_by_visible_text(text)

    def select_by_value(self, elemtarget, value):
        """
        根据选择框的属性值进行选择
        :param elemtarget:
        :param value:
        :return:
        """
        Select(self.get_element(elemtarget)).select_by_value(value)

    def get_element_text(self, elemtarget):
        """
        获取元素中的文本
        :param elemtarget:
        :return:
        """
        return self.get_element(elemtarget).text

    def save_Screenshot(self, scrfilename):
        """
        截图
        :param scrfilename:
        :return:
        """
        self.driver.get_screenshot_as_file(scrfilename)
    def keyboard_input(self, elemtarget, keyboardaction, value= None):
        """
        键盘输入：elemtarget, Keys.CONTROL, 'a'
        :param elemtarget:
        :param keyboardaction:
        :param value:
        :return:
        """
        self.webwait(elemtarget)
        self.driver.find_element(elemtarget).send_keys(keyboardaction, value)
    def mouse_operation_click_release(self, elemtarget):
        """
        鼠标点击元素，点击后释放
        :param elemtarget:
        :return:
        """
        ele_target = self.get_element(elemtarget)
        ActionChains(self.driver).click_and_hold(ele_target).release().perform()



    def webquit(self):
        """
        退出浏览器进程
        :return:
        """
        self.driver.quit()


if __name__ == '__main__':
    ff = Base('Chrome').get_url('http://127.0.0.1/ranzhi/sys/user-login-L3JhbnpoaS9zeXMvdXNlci1jcmVhdGUuaHRtbA==.html')

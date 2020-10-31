from common.print_log import add_log
from pageaction.switchto_iframe import Switch_to_iframe


class Adduser_ranzhi(Switch_to_iframe):

    def add_username(self, username):
        """
        输入用户名
        :param username:
        :return:
        """
        self.element_sendkeys('i, account', username)
    def add_realname(self, realname):
        """
        输入真实姓名
        :param realname:
        :return:
        """
        self.element_sendkeys('i, realname', realname)


    def chiose_sex(self, indx):
        """
        性别选择，0为男性，1为女性
        :param indx:
        :return:
        """
        self.elements_click('c,radio-inline', indx)

    def chiose_dep(self, text):
        """
        通过部门名字进行部门选择
        :param text:
        :return:
        """
        self.select_by_text('x,//*[@id="dept"]', text)

    def chiose_roles(self, text):
        """
        通过文本选择角色
        :param text:
        :return:
        """
        self.select_by_text('x,//*[@id="role"]', text)

    def send_pwd1(self, pw1):
        """
        输入密码1
        :param pw1:
        :return:
        """
        self.element_sendkeys('i,password1', pw1)

    def send_pwd2(self, pw2):
        """
        输入密码2
        :param pw2:
        :return:
        """
        self.element_sendkeys('i,password2', pw2)
    def add_email_address(self, email_address):
        """
        输入邮箱地址
        :param email_address:
        :return:
        """
        self.element_sendkeys('i,email', email_address)

    def click_button_save(self):
        """
        点击保存按钮
        :return:
        """
        self.element_click('i,submit')

    def set_num_of_pages(self, value):
        """
        输入页码，且切换到该页码界面
        :param elemtarget:
        :param value:
        :return:
        """
        self.element_sendkeys('x,//*[@id="_pageID"]', value)
        self.element_click('i,goto')

    def assertadduser(self, elemtarget, expected):
        try:
            # 取出要断言的文本，实际结果
            jieguo = self.get_element_text(elemtarget)
            add_log().info('取出文本成功：{}'.format(jieguo))
        except:
            add_log().error('文本提取失败')
            raise Exception
        try:
            assert jieguo == expected
            add_log().info("断言成功，实际结果：{}等于预期结果：{}".format(jieguo, expected))
        except:
            add_log().error("断言失败，实际结果：{}等于预期结果：{}".format(jieguo, expected))
            raise AssertionError




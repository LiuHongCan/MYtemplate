import datetime
import unittest
from parameterized import parameterized
from common.database_connect import get_databasedata
from common.print_log import add_log
from common.read_yaml import read_yaml_data
from common.readini import Get_ini_data
from pageaction.ranzhiadduser import Adduser_ranzhi


class Addusertest(unittest.TestCase):

    def setUp(self):
        url = 'http://127.0.0.1/ranzhi/sys/user-login.html'
        browserType = 'Chrome'
        self.addtest = Adduser_ranzhi(url=url, browserType=browserType)
        name = 'admin'
        pwd = '123456'
        self.addtest.user_login(name=name, pwd=pwd)
        clicktarget = 'x, //*[@id="s-menu-superadmin"]/button'
        self.addtest.element_click(clicktarget)
        elemtarget = 'i,iframe-superadmin'
        self.addtest.switch_to_web_iframe(elemtarget)
        self.addtest.element_click('x, //*[@id="shortcutBox"]/div/div[1]/div/a/h3')

    def tearDown(self):
        self.addtest.webquit()

    # 数据驱动，使用第3方的parameterized
    @parameterized.expand(read_yaml_data()['test01'])
    @unittest.skip("跳过")
    def test01(self, name, realname, sex, dep, roles, pwd1, pwd2, emailaddress):
        """
        添加成功的用例
        :param name:
        :param realname:
        :param sex:
        :param dep:
        :param roles:
        :param pwd1:
        :param pwd2:
        :param emailaddress:
        :return:
        """
        try:
            tt = str(datetime.datetime.now().microsecond)
            self.addtest.add_username(name + tt)
            add_log().info('用户名输入成功 {}'.format(name + tt))
            self.addtest.add_realname(realname)
            add_log().info('真实姓名输入成功 {}'.format(realname))
            self.addtest.chiose_sex(int(sex))
            add_log().info('性别选择成功 {}'.format(sex))
            self.addtest.chiose_dep(dep)
            add_log().info('部门选择成功 {}'.format(dep))
            self.addtest.chiose_roles(roles)
            add_log().info('角色选择成功 {}'.format(roles))
            self.addtest.send_pwd1(pwd1)
            add_log().info('密码1输入成功 {}'.format(pwd1))
            self.addtest.send_pwd2(pwd2)
            add_log().info('密码2输入成功 {}'.format(pwd2))
            self.addtest.add_email_address(tt + emailaddress)
            add_log().info('邮箱输入成功 {}'.format(tt + emailaddress))
            self.addtest.click_button_save()
            add_log().info('保存成功')
            self.addtest.set_num_of_pages(1000)
            add_log().info('页面切换成功')
            # 获取最后一条信息的用户名称文本
            usernamedata = self.addtest.get_element_text \
                (
                    'css,body > div > div > div > div.col-md-10 > div > div > table > tbody > tr:last-child > td:nth-child(3)')
            add_log().info('页面用户名称文本获取：{}'.format(usernamedata))
            self.assertEqual(name + tt, usernamedata, '客户验证添加失败')
            # 获取数据库信息，username
            actual_results = get_databasedata('select account from sys_user order by sys_user.join')
            add_log().info('数据库连接成功，数据：{}'.format(actual_results))
            self.assertEqual(name + tt, actual_results, '数据库验证添加失败')
        except:
            self.addtest.save_Screenshot(Get_ini_data().get_screenshot_path())
            add_log().error('执行失败')
            raise AssertionError


    @parameterized.expand(read_yaml_data()['test02'])
    @unittest.skip("跳过")
    def test02(self, name, realname, sex, dep, roles, pwd1, pwd2, emailaddress, expected):
        """
        用户名为空格或者特殊字符的测试用例
        :param name:
        :param realname:
        :param sex:
        :param dep:
        :param roles:
        :param pwd1:
        :param pwd2:
        :param emailaddress:
        :return:
        """
        try:
            tt = str(datetime.datetime.now().microsecond)
            self.addtest.add_username(name)
            add_log().info('用户名输入成功 {}'.format(name))
            self.addtest.add_realname(realname)
            add_log().info('真实姓名输入成功 {}'.format(realname))
            self.addtest.chiose_sex(int(sex))
            add_log().info('性别选择成功 {}'.format(sex))
            self.addtest.chiose_dep(dep)
            add_log().info('部门选择成功 {}'.format(dep))
            self.addtest.chiose_roles(roles)
            add_log().info('角色选择成功 {}'.format(roles))
            self.addtest.send_pwd1(pwd1)
            add_log().info('密码1输入成功 {}'.format(pwd1))
            self.addtest.send_pwd2(pwd2)
            add_log().info('密码2输入成功 {}'.format(pwd2))
            self.addtest.add_email_address(tt + emailaddress)
            add_log().info('邮箱输入成功 {}'.format(tt + emailaddress))
            self.addtest.click_button_save()
            add_log().info('点击保存')
            expected = expected
            # 获取输入框的提示文本
            actual_results = self.addtest.get_element_text('x,//*[@id="accountLabel"]')
            add_log().info('预期结果:{}---实际结果:{}'.format(expected, actual_results))
            self.assertEqual(expected, actual_results, '与预期结果不等')
        except:
            add_log().error('执行失败')
            self.addtest.save_Screenshot(Get_ini_data().get_screenshot_path())
            raise AssertionError


    @parameterized.expand(read_yaml_data()['test03'])
    @unittest.skip("跳过")
    def test03(self, name, realname, sex, dep, roles, pwd1, pwd2, emailaddress, expected):
        """
        用户名为空的测试用例
        :param name:
        :param realname:
        :param sex:
        :param dep:
        :param roles:
        :param pwd1:
        :param pwd2:
        :param emailaddress:
        :return:
        """
        try:
            tt = str(datetime.datetime.now().microsecond)
            self.addtest.add_username(name)
            add_log().info('用户名输入成功 {}'.format(name))
            self.addtest.add_realname(realname)
            add_log().info('真实姓名输入成功 {}'.format(realname))
            self.addtest.chiose_sex(int(sex))
            add_log().info('性别选择成功 {}'.format(sex))
            self.addtest.chiose_dep(dep)
            add_log().info('部门选择成功 {}'.format(dep))
            self.addtest.chiose_roles(roles)
            add_log().info('角色选择成功 {}'.format(roles))
            self.addtest.send_pwd1(pwd1)
            add_log().info('密码1输入成功 {}'.format(pwd1))
            self.addtest.send_pwd2(pwd2)
            add_log().info('密码2输入成功 {}'.format(pwd2))
            self.addtest.add_email_address(tt + emailaddress)
            add_log().info('邮箱输入成功 {}'.format(tt + emailaddress))
            self.addtest.click_button_save()
            add_log().info('点击保存')
            expected = expected
            # 获取输入框的提示文本
            actual_results = self.addtest.get_element_text('x,//*[@id="accountLabel"]')
            add_log().info('预期结果:{}---实际结果:{}'.format(expected, actual_results))
            self.assertEqual(expected, actual_results, '与预期结果不等')
        except:
            add_log().error('执行失败')
            self.addtest.save_Screenshot(Get_ini_data().get_screenshot_path())
            raise AssertionError


    @parameterized.expand(read_yaml_data()['test04'])
    @unittest.skip("跳过")
    def test04(self, name, realname, sex, dep, roles, pwd1, pwd2, emailaddress, expected):
        """
        用户名为空的测试用例
        :param name:
        :param realname:
        :param sex:
        :param dep:
        :param roles:
        :param pwd1:
        :param pwd2:
        :param emailaddress:
        :return:
        """
        try:
            tt = str(datetime.datetime.now().microsecond)
            self.addtest.add_username(name)
            add_log().info('用户名输入成功 {}'.format(name))
            self.addtest.add_realname(realname)
            add_log().info('真实姓名输入成功 {}'.format(realname))
            self.addtest.chiose_sex(int(sex))
            add_log().info('性别选择成功 {}'.format(sex))
            self.addtest.chiose_dep(dep)
            add_log().info('部门选择成功 {}'.format(dep))
            self.addtest.chiose_roles(roles)
            add_log().info('角色选择成功 {}'.format(roles))
            self.addtest.send_pwd1(pwd1)
            add_log().info('密码1输入成功 {}'.format(pwd1))
            self.addtest.send_pwd2(pwd2)
            add_log().info('密码2输入成功 {}'.format(pwd2))
            self.addtest.add_email_address(tt + emailaddress)
            add_log().info('邮箱输入成功 {}'.format(tt + emailaddress))
            self.addtest.click_button_save()
            add_log().info('点击保存')
            expected = expected
            # 获取输入框的提示文本
            actual_results = self.addtest.get_element_text('x,//*[@id="accountLabel"]')
            add_log().info('预期结果:{}---实际结果:{}'.format(expected, actual_results))
            self.assertEqual(expected, actual_results, '与预期结果不等')
        except:
            add_log().error('执行失败')
            self.addtest.save_Screenshot(Get_ini_data().get_screenshot_path())
            raise AssertionError


    @parameterized.expand(read_yaml_data()['test05'])
    @unittest.skip("跳过")
    def test05(self, name, realname, sex, dep, roles, pwd1, pwd2, emailaddress, expected):
        """
        真实姓名名为空的测试用例
        :param name:
        :param realname:
        :param sex:
        :param dep:
        :param roles:
        :param pwd1:
        :param pwd2:
        :param emailaddress:
        :return:
        """
        try:
            tt = str(datetime.datetime.now().microsecond)
            self.addtest.add_username(name)
            add_log().info('用户名输入成功 {}'.format(name))
            self.addtest.add_realname(realname)
            add_log().info('真实姓名输入成功 {}'.format(realname))
            self.addtest.chiose_sex(int(sex))
            add_log().info('性别选择成功 {}'.format(sex))
            self.addtest.chiose_dep(dep)
            add_log().info('部门选择成功 {}'.format(dep))
            self.addtest.chiose_roles(roles)
            add_log().info('角色选择成功 {}'.format(roles))
            self.addtest.send_pwd1(pwd1)
            add_log().info('密码1输入成功 {}'.format(pwd1))
            self.addtest.send_pwd2(pwd2)
            add_log().info('密码2输入成功 {}'.format(pwd2))
            self.addtest.add_email_address(tt + emailaddress)
            add_log().info('邮箱输入成功 {}'.format(tt + emailaddress))
            self.addtest.click_button_save()
            add_log().info('点击保存')
            expected = expected
            # 获取输入框的提示文本
            actual_results = self.addtest.get_element_text('x,//*[@id="realnameLabel"]')
            add_log().info('预期结果:{}---实际结果:{}'.format(expected, actual_results))
            self.assertEqual(expected, actual_results, '与预期结果不等')
        except:
            add_log().error('执行失败')
            self.addtest.save_Screenshot(Get_ini_data().get_screenshot_path())
            raise AssertionError


    @parameterized.expand(read_yaml_data()['test06'])
    @unittest.skip("跳过")
    def test06(self, name, realname, sex, dep, roles, pwd1, pwd2, emailaddress, expected):
        """
        真实姓名超过长度限制的测试用例
        :param name:
        :param realname:
        :param sex:
        :param dep:
        :param roles:
        :param pwd1:
        :param pwd2:
        :param emailaddress:
        :return:
        """
        try:
            tt = str(datetime.datetime.now().microsecond)
            self.addtest.add_username(name)
            add_log().info('用户名输入成功 {}'.format(name))
            self.addtest.add_realname(realname)
            add_log().info('真实姓名输入成功 {}'.format(realname))
            self.addtest.chiose_sex(int(sex))
            add_log().info('性别选择成功 {}'.format(sex))
            self.addtest.chiose_dep(dep)
            add_log().info('部门选择成功 {}'.format(dep))
            self.addtest.chiose_roles(roles)
            add_log().info('角色选择成功 {}'.format(roles))
            self.addtest.send_pwd1(pwd1)
            add_log().info('密码1输入成功 {}'.format(pwd1))
            self.addtest.send_pwd2(pwd2)
            add_log().info('密码2输入成功 {}'.format(pwd2))
            self.addtest.add_email_address(tt + emailaddress)
            add_log().info('邮箱输入成功 {}'.format(tt + emailaddress))
            self.addtest.click_button_save()
            add_log().info('点击保存')
            expected = expected
            # 获取输入框的提示文本
            actual_results = self.addtest.get_element_text('x,//*[@id="realnameLabel"]')
            add_log().info('预期结果:{}---实际结果:{}'.format(expected, actual_results))
            self.assertEqual(expected, actual_results, '与预期结果不等')
        except:
            add_log().error('执行失败')
            self.addtest.save_Screenshot(Get_ini_data().get_screenshot_path())
            raise AssertionError

    @parameterized.expand(read_yaml_data()['test07'])
    @unittest.skip("跳过")
    def test07(self, name, realname, sex, dep, roles, pwd1, pwd2, emailaddress, dept_value):
        """
        部门选择
        :param name:
        :param realname:
        :param sex:
        :param dep:
        :param roles:
        :param pwd1:
        :param pwd2:
        :param emailaddress:
        :return:
        """
        try:
            tt = str(datetime.datetime.now().microsecond)
            self.addtest.add_username(name+tt)
            add_log().info('用户名输入成功 {}'.format(name))
            self.addtest.add_realname(realname)
            add_log().info('真实姓名输入成功 {}'.format(realname))
            self.addtest.chiose_sex(int(sex))
            add_log().info('性别选择成功 {}'.format(sex))
            self.addtest.chiose_dep(dep)
            add_log().info('部门选择成功 {}'.format(dep))
            self.addtest.chiose_roles(roles)
            add_log().info('角色选择成功 {}'.format(roles))
            self.addtest.send_pwd1(pwd1)
            add_log().info('密码1输入成功 {}'.format(pwd1))
            self.addtest.send_pwd2(pwd2)
            add_log().info('密码2输入成功 {}'.format(pwd2))
            self.addtest.add_email_address(tt + emailaddress)
            add_log().info('邮箱输入成功 {}'.format(tt + emailaddress))
            self.addtest.click_button_save()
            add_log().info('点击保存')
            expected = dep
            self.addtest.set_num_of_pages(1000)
            actual_results = self.addtest.get_element_text\
                ('css,body > div > div > div > div.col-md-10 > div > div > table > tbody > tr:last-child > td:nth-child(5)')
            add_log().info('获取部门名称{}'.format(actual_results))
            self.assertEqual(expected, actual_results, '与预期结果不等')
            # 获取数据库中最新一条记录的部门信息
            databasedata = get_databasedata('select sys_user.dept from sys_user order by sys_user.join')
            self.assertEqual(dept_value, databasedata, '实际部门{}与数据库数据{}比较'.format(dept_value, databasedata))
            add_log().info('数据库验证成功:输入值：{}与数据库记录：{}'.format(dept_value, databasedata))

        except:
            add_log().error('执行失败')
            self.addtest.save_Screenshot(Get_ini_data().get_screenshot_path())
            raise AssertionError

    @parameterized.expand(read_yaml_data()['test08'])
    @unittest.skip("跳过")
    def test08(self, username, realname , pwd1, pwd2, emailaddress, elemtarget, expected):
        """
        将断言封装成一个函数
        :param username:
        :param realname:
        :param pwd1:
        :param pwd2:
        :param emailaddress:
        :param elemtarget:
        :param expected:
        :return:
        """
        try:
            self.addtest.add_username(username)
            self.addtest.add_realname(realname)
            self.addtest.send_pwd1(pwd1)
            self.addtest.send_pwd2(pwd2)
            self.addtest.add_email_address(emailaddress)
            self.addtest.click_button_save()
            self.addtest.assertadduser(elemtarget, expected)
        except:
            raise AssertionError

    @parameterized.expand(read_yaml_data()['test09'])
    def test09(self, username, realname, pwd1, pwd2, emailaddress, elemtarget, expected):
        """
        直接传入要断言的元素取出其文本
        :param username:
        :param realname:
        :param pwd1:
        :param pwd2:
        :param emailaddress:
        :param elemtarget:
        :param expected:
        :return:
        """
        try:
            self.addtest.add_username(username)
            self.addtest.add_realname(realname)
            self.addtest.send_pwd1(pwd1)
            self.addtest.send_pwd2(pwd2)
            self.addtest.add_email_address(emailaddress)
            self.addtest.click_button_save()
            shijijieguo = self.addtest.get_element_text(elemtarget)
            self.assertEqual(shijijieguo, expected, '实际结果：{}--预期结果{}'.format(shijijieguo, expected))
        except:
            # add_log().error('实际结果：{}--预期结果{}'.format(shijijieguo, expected))
            raise AssertionError



if __name__ == '__main__':
     unittest.main()

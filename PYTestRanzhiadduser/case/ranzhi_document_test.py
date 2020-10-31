import datetime
import unittest
from parameterized import parameterized
from common.print_log import add_log
from common.readini import Get_ini_data
from common.red_jsondata import readjsondata
from pageaction.ranzhi_documont import RanzhiDocument


class Document_Operation(unittest.TestCase):

    def setUp(self):
        url = 'http://127.0.0.1/ranzhi/sys/user-login.html'
        browserType = 'Chrome'
        self.document = RanzhiDocument(url=url, browserType=browserType)
        name = 'admin'
        pwd = '123456'
        self.document.user_login(name=name, pwd=pwd)
        clicktarget = 'x, //*[@id="s-menu-superadmin"]/button'
        self.document.element_click(clicktarget)
        # 进入文档管理界面
        self.document.enter_douumentmod()
        add_log().info('进入文档管理界面')

    def tearDown(self):
        self.document.webquit()

    @parameterized.expand(readjsondata()['test01'])
    def test01(self, doclibtyp, doclibname, groupnum):
        """
        添加文档库的测试
        :param doclibtyp:
        :param doclibname:
        :param groupnum:
        :return:
        """
        try:
            tt = datetime.datetime.now().microsecond
            tt = str(tt)
            # 创建文档库
            # 选择iframe框架
            self.document.select_doc_ifarme()
            add_log().info('进入iframe框架')
            # 进入到文档库添加界面
            self.document.cteat_doc_mod()
            add_log().info('进入到创建文档库界面')
            # 选择文档库类型
            self.document.select_doc_lib(doclibtyp)
            add_log().info('文档库类型选择为:{}'.format(doclibtyp))
            # 写入文档库名字
            self.document.set_doclib_name(doclibname+tt)
            add_log().info('文档库名字为{}'.format(doclibname+tt))
            # 根据li标签序号选择几个用户来使用文档库
            self.document.set_username_doclib(1, 14, 3)
            add_log().info('用户选择完成')
            # 根据class下标选择授权分组，可以多选
            self.document.chiose_usergroup(groupnum)
            add_log().info('用户组选择为：{}'.format(groupnum))
            # 点击保存按钮
            self.document.click_savecreatdoc_buttom()
            add_log().info('保存按钮点击操作')
            self.document.out_doc_ifarme()
            self.document.reload_doc_window()
            self.document.select_doc_ifarme()
            # 切换到文档库首页
            self.document.switch_doc_home()
            add_log().info('切换到文档库首页')
            libname = self.document.get_element_text('css,#libs > div > div:nth-child(1) > div > a')
            add_log().info('首页第一个新文档名字：{}，输入的文档名字{}'.format(libname, doclibname+tt))
            self.assertEqual(libname, doclibname+tt, '客户端验证添加文档库失败')
        except:
            self.document.save_Screenshot(Get_ini_data().get_screenshot_path())
            raise AssertionError


if __name__ == '__main__':
    unittest.main()

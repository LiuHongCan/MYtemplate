from time import sleep

from pageaction.userlogin import User_login


class RanzhiDocument(User_login):

    def enter_douumentmod(self):
        """
        进入文档管理模块
        :return:
        """
        self.element_click('x,//*[@id="s-menu-4"]/button/img')
    def select_doc_ifarme(self):
        """
        选择到文档界面的iframe框架
        :return:
        """
        self.switch_to_iframe('i,iframe-4')
    def out_doc_ifarme(self):
        """
        退出当前iframe
        :return:
        """
        self.driver.switch_to.default_content()



    def switch_doc_home(self):
        """
        切换到文档首页
        :return:
        """

        self.element_click('x,//*[@id="mainNavbar"]/ul/li[1]/a')
    def switch_doc_project(self):
        """
        切换到项目文档库
        :return:
        """

        self.element_click('x,//*[@id="mainNavbar"]/ul/li[2]/a')

    def switch_doc_custom(self):
        """
        切换到用户自定义文档库
        :return:
        """

        self.element_click('x,//*[@id="mainNavbar"]/ul/li[3]/a')
    def min_doc_window(self):
        """
        最小化文档窗口
        :return:
        """
        self.element_click('x,//*[@id="win-4"]/div[1]/ul/li[2]/button')
    def max_doc_window(self):
        """
        最大化文档窗口
        :return:
        """
        self.out_doc_ifarme()
        self.element_click('x,//*[@id="s-task-4"]/button')

    def reload_doc_window(self):
        """
        刷新文档窗口
        :return:
        """

        self.element_click('x,//*[@id="win-4"]/div[1]/ul/li[1]/button')

    def close_doc_window(self):
        """
        关闭文档窗口
        :return:
        """

        self.element_click('x,//*[@id="win-4"]/div[1]/ul/li[4]/button')

    def cteat_doc_mod(self):
        """
        进入创建文档模块
        :return:
        """

        self.element_click('i, createButton')

    def exit_creatdoc_mod(self):
        """
        退出文档库创建框
        :return:
        """
        self.element_click('x,//*[@id="ajaxModal"]/div[2]/div/div[1]/button')
    def select_doc_lib(self, text):
        """
        选择文档库
        :param text:
        :return:
        """
        self.select_by_text('x,//*[@id="libType"]', text)
    def set_doclib_name(self, doclibname):
        """
        输入文档库名称
        :param doclibname:
        :return:
        """
        self.element_sendkeys('x,//*[@id="name"]', doclibname)
    def set_username_doclib(self,*liindex):
        """
        根据li标签序号选择用户名
        :param :
        :return:
        """
        # self.mouse_operation_click_release('x,//*[@id="users_chosen"]/ul')
        self.inputnum = list(liindex)

        for i in range(len(self.inputnum)):

            self.mouse_operation_click_release('x,//*[@id="users_chosen"]/ul')
            self.get_element('x,//*[@id="users_chosen"]/div/ul').find_elements_by_tag_name('li')[self.inputnum[i]].click()




    # def set_username_doclib_clear(self, num):
    #     """
    #     清空输入框
    #     :return:
    #     """
    #     if 0< num <= self.inputnum:
    #         self.element_click('x,//*[@id="users_chosen"]/ul/li[{}]/a'.format(num))
    #     else:
    #         print('要删除的角色错误')

    def chiose_usergroup(self, indx):
        """
        选择用户授权分组，根据class属性下标选择
        :param indx:
        :return:
        """
        self.elements_click('class,checkbox-inline', indx)
    def click_savecreatdoc_buttom(self):
        """
        点击保存文档库按钮
        :return:
        """
        self.element_click('x,//*[@id="submit"]')
    def click_docdir(self, indx):
        """
        根据class下标选择文档目录
        :param indx:
        :return:
        """
        self.elements_click('c,lib lib-custom', indx)
    def click_creatdoc_button(self):
        """
        点击创建文档按钮，此按钮在iframe框架中
        :return:
        """
        self.element_click('x,//*[@id="menuActions"]/a')


from pageaction.userlogin import User_login


class Switch_to_iframe(User_login):

    def switch_to_web_iframe(self, elemtarget):
        """
        选择网页中要切换的iframe框架
        :return:
        """
        self.switch_to_iframe(elemtarget)
    def click_iframe_element(self, elemtarget):
        """
        点击网页中iframe中的元素
        :param elemtarget:
        :return:
        """
        self.element_click(elemtarget)



if __name__ == '__main__':
    elemtarget =  'i,iframe-superadmin'
    url = 'http://127.0.0.1/ranzhi/sys/user-login.html'
    ss = Switch_to_iframe(url,'Chrome')
    ss.user_login('admin','123456')
    ss.element_click('x, //*[@id="s-menu-superadmin"]/button')
    ss.switch_to_web_iframe(elemtarget)
    ss.click_iframe_element('x, //*[@id="shortcutBox"]/div/div[1]/div/a/h3')
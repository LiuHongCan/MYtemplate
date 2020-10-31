from pageaction.openurl import Open_url


class User_login(Open_url):

    def user_login(self, name, pwd):
        """
        用户登录
        :param name:
        :param pwd:
        :return:
        """
        self.elements_sendkeys('c,form-control', name, indx=0)
        self.elements_sendkeys('c,form-control', pwd, indx=1)
        self.element_click('i,submit')

    def user_logout(self):
        """
        点击签退，登出系统
        :return:
        """
        self.element_click('x, //*[@id="bottomRightBar"]/ul/li[1]/a')


if __name__ == '__main__':
    url = 'http://127.0.0.1/ranzhi/sys/user-login-L3JhbnpoaS9zeXMvdXNlci1jcmVhdGUuaHRtbA==.html'
    tt = User_login(url=url, browserType='Chrome')
    tt.user_login('admin', '123456')
    tt.user_logout()


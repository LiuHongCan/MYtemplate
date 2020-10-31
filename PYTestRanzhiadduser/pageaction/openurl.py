from common.Bases import Base


class Open_url(Base):
    """
    初始化打开网址
    """
    def __init__(self, url, browserType):
        Base.__init__(self, browserType)
        self.browserType = browserType
        self.url = url
        self.get_url(url)
        self.maxwindow()
    # def user_login(self, name, pwd):
    #     print(self.get_by_param('c,form-control'))
    #     self.elements_sendkeys('c,form-control', name, indx=0)
    #     self.elements_sendkeys('c,form-control', pwd, indx=1)





if __name__ == '__main__':
    logranzhi = Open_url('http://127.0.0.1/ranzhi/sys/user-login-L3JhbnpoaS9zeXMvdXNlci1jcmVhdGUuaHRtbA==.html'
                         , 'Chrome')

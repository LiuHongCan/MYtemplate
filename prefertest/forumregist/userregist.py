import re

import requests


def add_forum_user():
    session = requests.Session()
    headers = {"User-Agent":
                   "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) "
                   "like Gecko Core/1.70.3775.400 QQBrowser/10.6.4208.400"}

    url = "http://192.168.35.135:8080/jforum-2.6.2/jforum.page"
    url2 = "http://192.168.35.135:8080/jforum-2.6.2/user/logout.page"
    urltoken = "http://192.168.35.135:8080/jforum-2.6.2/user/acceptAgreement.page"

    username = None
    email = None
    token = None
    datas = {"action": "insertSave",
             "module": "user",
             "username": username,
             "OWASP_CSRFTOKEN": token,
             "email": email,
             "password": "1",
             "password_confirm": "1",
             "submit": "确定"}
    for id in range(300, 450):
        username = "test01{}".format(id)
        email = "100{}@163.com".format(id)
        response = session.get(url=urltoken, headers=headers).text
        res1 = 'name="OWASP_CSRFTOKEN" value="(.+?)" />'
        token = re.findall(res1, response)[0]

        datas["OWASP_CSRFTOKEN"] = token
        datas["username"] = username
        datas["email"] = email
        session.post(url=url, data=datas, headers=headers)
        # session.get(url=url2)


if __name__ == '__main__':
    add_forum_user()

    # urls = "http://192.168.109.136:8080/jforum-2.6.2/user/acceptAgreement.page"
    # session = requests.Session()
    # headers = {"User-Agent":
    #                "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) "
    #                "like Gecko Core/1.70.3775.400 QQBrowser/10.6.4208.400"}
    # response = session.get(url=urls,headers=headers).text
    # rrrr = response.text
    # res1 = 'name="OWASP_CSRFTOKEN" value="(.+?)" />'
    # k = re.findall(res1, rrrr)[0]
    # print(k)

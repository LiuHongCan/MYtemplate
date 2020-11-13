import requests


def add_user_nmae():
    session = requests.Session()

    logurl = "http://192.168.35.135:8080/korei/login.ht"

    headers = {"User-Agent":
                   "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) "
                   "like Gecko Core/1.70.3775.400 QQBrowser/10.6.4208.400"}

    data = {"username": "admin",
            "password": "1"}

    session.post(url=logurl, data=data, headers=headers)

    addurl = "http://192.168.35.135:8080/korei/platform/system/sysUser/save.ht?selectedOrgId= "

    username1 = "test10"
    addata2 = {"changePwd": "true",
               "userRole": "6",
               "account": username1,
               "birthday": "2020-11-12",
               "mobile": "13456778989",
               "fullname": "老王",
               "storeId": "",
               "status": "1",
               "password": "1",
               "sex": "1",
               "level": "0",
               "phone": "",
               "address": "",
               "qq": "",
               "email": "",
               "weixinid": "",
               "entryDate": "",
               "userId": ""}


    for id in range(401, 452):
        username1 = "test10{}".format(id)
        addata2["account"]= username1
        session.post(url=addurl, data=addata2, headers=headers)



if __name__ == '__main__':
    add_user_nmae()


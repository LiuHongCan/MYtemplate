import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendemails(filepath):
    try:
        # 配置服务器
        smtpsever = 'smtp.163.com'
        # 邮箱端口
        serverport = '25'
        # 设置发件人
        sender = '15681125117@163.com'
        # 设置收件人
        receiver = '15681125117@163.com,2270925030@qq.com'

        # 授权码
        pwd = 'NHDSUDADYBYOEEYF'
        # 创建邮件对象
        msgs = MIMEMultipart()
        msgs['From'] = sender
        msgs['To'] = receiver
        msgs['Subject'] = '然之测试报告'

        # 打开并读取报告内容
        with open(filepath, 'rb') as fp:
            bodys = fp.read()
        # 写入正文
            bodytext = MIMEText(bodys, 'html', 'utf-8')
        # 将正文加入邮件中
        # msgs.attach(MIMEText("本轮测试报告","plain","utf-8"))
            msgs.attach(bodytext)

        # # 将报告写入附件中
            att = MIMEText(bodys, 'base64', 'utf-8')
            att['Content-Type'] = 'application/octet-stream'
            att['Content-Disposition'] = 'attachment;filename = "testreport.html"'
            msgs.attach(att)

        # 构造附件1，传送当前目录下的 test.txt 文件
        # att1 = MIMEText(open(filepath, 'rb').read(), 'base64', 'utf-8')
        # att1["Content-Type"] = 'application/octet-stream'
        # # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        # att1["Content-Disposition"] = 'attachment; filename="testreport.html"'
        # msgs.attach(att1)

        # 进行邮件发送
        # 创建服务器对象
        smtp = smtplib.SMTP()
        # 链接服务器
        smtp.connect(smtpsever, serverport)
        # 登录
        smtp.login(sender, pwd)
        # 发送邮件
        smtp.sendmail(sender, receiver.split(','), msgs.as_string())
    except:
        raise Exception

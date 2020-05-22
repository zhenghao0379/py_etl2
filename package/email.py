# 邮件配置
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from .config import *

class email_set:
    def __init__(self, mail_stmp = 'email_stmp'):
        mail_config = config.items(mail_stmp)
        self.host = config.get('email_stmp', 'host')
        self.port = config.getint('email_stmp', 'port')
        self.sender = config.get('email_stmp', 'sender')
        self.password = configp.get('email_stmp', 'password')
        self.license = configp.get('email_stmp', 'license')
    
    def sender_set(self, sender):
        self.sender = sender

    def send(self, mm):
        # 创建SMTP对象
        stp = smtplib.SMTP()
        # 设置发件人邮箱的域名和端口，端口地址为25
        stp.connect(self.mail_host, self.port)  
        # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
        stp.set_debuglevel(1)
        # 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
        stp.login(self.mail_sender, self.mail_license)
        # 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
        stp.sendmail(mail_sender, mail_receivers, mm.as_string())
        print("邮件发送成功")
        # 关闭SMTP对象
        stp.quit()

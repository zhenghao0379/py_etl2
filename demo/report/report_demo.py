import os
import sys
sys.path.append(os.getcwd())

# 自建环境
from package import * 

# 邮件配置
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "stmp.163.com"
mail_user = ""
mail_pass = ""

sender = "from@qq.com"
receiver = ['']

# 
from docx import Document
from docx.shared import Inches
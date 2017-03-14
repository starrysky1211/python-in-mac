import smtplib
import email.MIMEMultipart
import email.MIMEText
import os.path

# 构造邮件
msg = email.MIMEText('hello, send from Python! ', 'plain', 'utf-8')

# 替换成发送邮箱和接收邮箱以及文件名
From = "starry_sky_@outlook.com"
To = "meliuzheng@foxmail.com"
file_name = "file name"
password = input("password: ")
# 输入发送邮箱的服务器地址
server = smtplib.SMTP("smtp-mail.outlook.com", 587)
# 调试设定
server.set_debuglevel(1)
# 登陆服务器
server.login(From, str(password))
server.sendmail(From, To, msg.as_string())
server.quit()

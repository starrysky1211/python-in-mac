# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


mail_to_list = ['starry_sky_@outlook.com']
mail_host = "smtp.163.com"
mail_user = "15652826118"
mail_pass = "sunny1231"
mail_postfix = "163.com"


def send_mail(to_list, sub, content):
    me = "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)

    body = MIMEText(content, "plain", 'utf-8')
    msg.attach(body)

    with open('/Users/starrysky/GitHub/hexo/_config.yml', 'rb') as f:
        mime = MIMEBase('file', 'yml', filename='_config.yml')

        mime.add_header('Content-Disposition', 'attachment', filename='_config.yml')
        mime.set_payload(f.read())
        mime['Content-Type'] = 'application/octet-stream'

        msg.attach(mime)

    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print (str(e))
        return False


for i in range(1):
    if send_mail(mail_to_list, "text-mail", "有没有附件？"):
        print "done! "
    else:
        print "failed! "

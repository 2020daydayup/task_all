import smtplib
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders




def send_mail():
    smtp = SMTP_SSL("smtp.geneplus.org.cn", 25)
    smtp.set_debuglevel(1)
    smtp.ehlo("smtp.geneplus.org.cn")
    smtp.login("project@geneplus.org.cn", "!@#qweASD")
    msg = MIMEText('0420测试1',"plain", "utf-8")
    msg["Subject"] = Header("邮件标题11", "utf-8")
    msg["from"] = "project@geneplus.org.cn"
    msg["to"] = "longxj@geneplus.org.cn"
    smtp.sendmail("project@geneplus.org.cn", "longxj@geneplus.org.cn", msg.as_string())
    smtp.quit()

# send_mail()
#!/usr/bin/python3import smtplib
# smtpObj = smtplib.SMTP( ["smtp.geneplus.org.cn" , 25 , local_hostname]]] )
sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

smtpObj = smtplib.SMTP(local_hostname="smtp.geneplus.org.cn", port=25)
smtpObj.sendmail(sender, receivers, message)





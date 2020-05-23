import configparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def memo_send_mail( data, username, tosb):
    "发送邮件"
    config = configparser.ConfigParser()
    config.read("config/mail.config")
    item = dict(config.items('mail'))
    s = smtplib.SMTP(host='smtp.geneplus.org.cn')
    s.connect(host=item['host'], port=item['port'])
    s.login(item['username'], item['password'])

    mesege = f"""
            hi {username}:</br>
            您的备忘录信息如下：</br>
            {data}</br>
             系统邮件，请勿回复</br>
             祝好~~
    """
    content = MIMEText(mesege, 'html', 'utf-8')
    msg = MIMEMultipart()
    msg['Subject'] = "备忘录"
    msg['From'] = 'project@geneplus.org.cn'
    msg['To'] = tosb
    msg.attach(content)
    s.send_message(msg)
    s.quit()
memo_send_mail("fsdfsafsaf", 'username', 'longxj@geneplus.org.cn')
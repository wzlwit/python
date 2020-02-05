# https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/14.%E7%BD%91%E7%BB%9C%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8%E5%92%8C%E7%BD%91%E7%BB%9C%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91.md

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = 'zhaolongw@mtygroup.com'
    # receivers = ['uvwxyz@qq.com', 'uvwxyz@126.com']
    receivers = ['zhaolongw@mtygroup.com']
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = Header('王大锤', 'utf-8')
    message['To'] = Header('骆昊', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.163.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'Talent!982mail')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


if __name__ == '__main__':
    main()
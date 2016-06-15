# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 16:00:05 2016

@author: 1
"""
import smtplib                               #python3.5에서는 smtplib 사용해도 됨
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart #MIMEMultipart MIME 생성
from email.mime.text import MIMEText

def mail_data(data):
    f = open("mail_data.html",'w')
    html_source = '''
    <html>
    <header></header>
    <body>
    <p>''' + data + '''
    </p>
    </body>
    </html>
    '''
    f.write(html_source)
    f.close()
    return "mail_data.html"

def send(ti, Addr, data):
    host = "smtp.gmail.com"  # Gmail SMTP 서버 주소.
    port = "587"

    title = ti
    senderAddr = "scriptlanguage2@gmail.com"  # senderAddr = str(input ('보내는 메일 주소 :'))
    recipientAddr = Addr
    passwd = "scriptlanguage"  # str(input ('보내는 메일 주소의 비밀번호 :'))

    msg = MIMEBase("multipart", 'alternative')  # Message container를 생성
    msg['Subject'] = title  # set message
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    htmlFD = open(mail_data(data), 'rb')
    htmlPart = MIMEText(htmlFD.read(), 'html', _charset='utf-8')
    htmlFD.close()

    msg.attach(htmlPart)  # 메세지에 생성한 MIME 문서를 첨부합니다
    print("SMTP 서버에 연결 중 ... ")
    s = smtplib.SMTP(host, port)  # python3.5에서는 smtplib.SMTP(host,port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)  # 로그인
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()
    print("메일을 전송하였습니다.")

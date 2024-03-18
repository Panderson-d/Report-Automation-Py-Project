#!/usr/bin/env python3

import psutil
import socket
import smtplib

if psutil.cpu_percent(1) > 80:
    from email.message import EmailMessage
    message = EmailMessage()
    sender = "automation@example.com"
    receiver = "student-03-ef3e8b274a0f@example.com"
    message['From'] = sender
    message['To'] = receiver
    #  replace username with your username
    subject = "Error - CPU usage is over 80%"
    message['Subject'] = subject
    body = "Please check your system and resolve the issue as soon as possible."
    message.set_content(body)
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    {}
    mail_server.quit()

if (psutil.virtual_memory()[1] / 1024 / 1024) < 500:
    from email.message import EmailMessage
    message = EmailMessage()
    sender = "automation@example.com"
    receiver = "student-03-ef3e8b274a0f@example.com"
    message['From'] = sender
    message['To'] = receiver
    subject = "Error - Available memory is less than 500MB"
    message['Subject'] = subject
    body = "Please check your system and resolve the issue as soon as possible."
    message.set_content(body)
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    {}
    mail_server.quit()


if psutil.disk_usage('/')[3] > 80:
    from email.message import EmailMessage
    message = EmailMessage()
    sender = "automation@example.com"
    receiver = "student-03-ef3e8b274a0f@example.com"
    message['From'] = sender
    message['To'] = receiver
    subject = "Error - Available disk space is less than 20%"
    message['Subject'] = subject
    body = "Please check your system and resolve the issue as soon as possible."
    message.set_content(body)
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    {}
    mail_server.quit()

def check_hostname():
    try:
        local_ip = socket.gethostbyname('localhost')
        return True
    except socket.gaierror:
        return False

if check_hostname():
    pass
else:
    from email.message import EmailMessage
    message = EmailMessage()
    sender = "automation@example.com"
    receiver = "student-03-ef3e8b274a0f@example.com"
    message['From'] = sender
    message['To'] = receiver
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message['Subject'] = subject
    body = "Please check your system and resolve the issue as soon as possible."
    message.set_content(body)
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    {}
    mail_server.quit()

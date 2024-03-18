#!/usr/bin/env python3

import os

from email.message import EmailMessage
message = EmailMessage()


sender = "automation@example.com"
receiver = "student-03-ef3e8b274a0f@example.com"
message['From'] = sender
message['To'] = receiver
subject = "Upload Completed - Online Fruit Store"
message['Subject'] = subject
body = "All fruits are uploaded to our website successfully.A detailed list is attached to this email."
message.set_content(body)

import os.path
attachment_path = "/tmp/processed.pdf"
attachment_filename = os.path.basename(attachment_path)
import mimetypes
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)

with open(attachment_path, 'rb') as ap:
     message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=os.path.basename(attachment_path))
     
import smtplib
mail_server = smtplib.SMTP('localhost')
mail_server.send_message(message)
{}
mail_server.quit()

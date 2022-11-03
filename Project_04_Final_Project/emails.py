#!/usr/bin/env python3

from email.message import EmailMessage
import os
import smtplib
import mimetypes

def generate_email(sender, recipient, subject, body, attachment):
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    attachment_filename = os.path.basename(attachment)
    mime_type, _ = mimetypes.guess_type(attachment)
    mime_type, mime_subtype = mime_type.split("/", 1)
    with open(attachment, 'rb') as ap:
        message.add_attachment(ap.read(), maintype = mime_type, subtype = mime_subtype, filename = os.path.basename(attachment))
    return message

def generate_error_report(sender, recipient, subject):
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    body = "Please check your system and resolve the issue as soon as possible."
    message.set_content(body)
    return message

def send_email(email):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(email)
    mail_server.quit()

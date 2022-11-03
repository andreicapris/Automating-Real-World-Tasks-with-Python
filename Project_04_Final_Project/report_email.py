#!/usr/bin/env python3

import os
import datetime
import reports
import emails
import re


directory_path = os.path.abspath(os.getcwd())
text_path = "supplier-data/descriptions"
txt_fp = os.path.join(directory_path, text_path)
txt_pattern = r"(\w)*.txt"
current_time = datetime.datetime().strftime("%B %d, %Y")

def gen_pdf_body(path):
    body = ""
    txt_list = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            if re.match(txt_pattern, filename):
                tmp_path = os.join(path, filename)
                txt_list = get_text(tmp_path)
                body += "<br/>" + "name: " + txt_list[0] + "<br/>" + "weight: " + txt_list[1] + "<br/>"
    return body

def get_text(path):
    txt_list = []
    with open(path) as file:
        for line in file.readlines():
            txt_list.append(line.strip())
    return txt_list

if __name__ == "__main__":
    title = "Process Updated on " + current_time
    body = gen_pdf_body(text_path)
    reports.generate_report("/tmp/processed.pdf", title, body)
    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ["USER"])
    subject = "Upload Completed - Online Fruit Store"
    email_body = "All fruits are uploaded to our website successfully. A detailed lis is attached to this email."
    attachment = "/tmp/processed.pdf"
    message = emails.generate_email(sender, recipient, subject, email_body, attachment)
    emails.send_email(message)

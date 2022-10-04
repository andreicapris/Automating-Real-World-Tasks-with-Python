"""This script creates the email adds summary as a pdf attachment and sends it when prompted"""

from email.message import EmailMessage
import smtplib
import getpass

def generate_email(summary):
    mail_server = smtplib.SMTP_SSL('advanced.ro')
    sender = "test@advanced.ro"
    recipient = "andrei.capris.sorin@gmail.com"
    message = EmailMessage()
    message['Subject'] = "Sales summary for last month"
    message['From'] = sender
    message['To'] = recipient
    message.set_content(summary)

    print("Would you like to send the email?")
    answer = input()
    if answer == "yes":
        mail_pass = getpass.getpass("Please input password for {}: ".format(sender))
        mail_server.login(sender, mail_pass)
        print("Sending email")
        mail_server.send_message(message)
        print("Closing connection")
        mail_server.quit()
    else:
        print("Exiting program")
        exit()

#    print(message)



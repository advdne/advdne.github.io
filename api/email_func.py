import smtplib


# Reference: https://pybit.es/python-smtplib.html
# sample call send_gmail(youngwk.alert2@gmail.com, "subject title contents", "body msg")
def send_gmail(recipient_email, subject_title, body_msg):
    import smtplib
    smtp_port = 587
    smtp_server = smtplib.SMTP('smtp.gmail.com', smtp_port)
    smtp_server.ehlo()
    smtp_server.starttls()
    # lightaiyee@gmail.com key for gmail
    # App password: fhqbjllopcywvpgp
    email_login = 'lightaiyee@gmail.com'
    # To create app password (assumes 2-step verification), https://support.google.com/accounts/answer/185833?hl=en
    google_app_password = 'fhqbjllopcywvpgp'
    smtp_server.login(email_login, google_app_password)
    sender_email = 'lightaiyee@gmail.com'

    smtp_server.sendmail(sender_email, recipient_email, 'Subject: ' + subject_title + '\n' + body_msg)
    smtp_server.quit()  # 1234

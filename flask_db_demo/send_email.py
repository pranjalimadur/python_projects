from email.mime.text import MIMEText
import smtplib

def send_email(em,he,avg_he,cnt):
    from_email="pranjalimadur@gmail.com"
    from_password="Pranj@li2801"
    to_email=em

    subject="Height data"
    message="Your height is <strong>%s</strong>! <br> Average height of all users is <strong>%s</strong> based on %s users <br> Thanks!"%(he,avg_he,cnt)

    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)

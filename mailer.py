import smtplib
import os
from email.mime.text import MIMEText

def send_mail(user):
  msg = MIMEText('Hello, your file upload was successful.')
  msg['Subject'] = 'File Upload Successful'
  msg['From'] = 'help@icd.com'
  msg['To'] = 'john@example.com'

  smtp_server = os.environ['MAILHOG_HOST']
  smtp_port = 1025

  with smtplib.SMTP(smtp_server, smtp_port) as server:
      server.sendmail(msg['From'], msg['To'], msg.as_string())

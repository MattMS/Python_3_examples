from email.mime.text import MIMEText
from smtplib import SMTP
import logging


#from settings import EMAIL_FROM, EMAIL_MSG, EMAIL_TO, SERVER
EMAIL_FROM = 'me@example.com'
EMAIL_MSG = 'Hi friend!'
EMAIL_SUBJECT = 'Hi'
EMAIL_TO = 'friend@example.com'
SERVER = 'smtp.example.com'


if __name__ == '__main__':
	msg = MIMEText(EMAIL_MSG)
	msg['Subject'] = EMAIL_SUBJECT
	msg['From'] = EMAIL_FROM
	msg['To'] = EMAIL_TO

	with SMTP(SERVER) as smtp:
		#smtp.sendmail(EMAIL_FROM, EMAIL_TO, EMAIL_MSG)
		smtp.send_message(msg)

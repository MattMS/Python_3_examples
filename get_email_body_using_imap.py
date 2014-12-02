import email
from imaplib import IMAP4_SSL
import quopri


# Called recursively.
def get_email_content(message):
	if not message.is_multipart():
		return message.get_payload()

	parts = [get_email_content(payload) for payload in message.get_payload()]
	return ''.join(parts)


server = 'imap.example.com'
username = 'matt'
password = 'Password1'

mail = IMAP4_SSL(server)
mail.login(username, password)

mail.select('INBOX')

ok, raw_uid_list = mail.uid('search', None, 'ALL')
if ok != 'OK':
	raise Exception('Bad')

uid_list = raw_uid_list[0].split()
uid = uid_list[0]

ok, data = mail.uid('fetch', uid, '(RFC822)')
if ok != 'OK':
	raise Exception('Bad')

raw_email_bytes = data[0][1]
email_message = email.message_from_bytes(raw_email_bytes)

raw_content = get_email_content(email_message)
content = quopri.decodestring(raw_content, False)
for line in content.splitlines():
	print(line)

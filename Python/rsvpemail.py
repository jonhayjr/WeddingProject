--Emails RSVPUpdates.csv which shows all updates that have been made.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 
email_password = 
email_send = 

subject = 'Modified Guest RSVPs and Notes'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi!  Here are the modified RSVPs and notes for today.'
msg.attach(MIMEText(body,'plain'))

filename='C:\\Exports\\RSVPUpdates.csv'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

try:
	msg.attach(part)
	server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
	server.login(email_user, email_password)
	text = msg.as_string()
	server.sendmail(email_user, email_send, text)
	server.quit()

	print ("Email sent!")

except:

	print ("Something went wrong.")

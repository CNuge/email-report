import smtplib
import socket
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders

""" info on where to message to and from """
fromaddr = 'xxxxxxxxx'
password = 'xxxxxx'
toaddr = 'xxxxx'

""" set up the message, get the to, from and subject input """
now = datetime.now()
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Your morning update for %s" % (now.strftime('%m/%d/%Y'))


""" here import compose message and build up the body of the text """
body = 

""" look at the docs here, see if you can change the 'plain' to alter the format """	
msg.attach(MIMEText(body, 'plain'))

""" connect to the gmail server, send the email """
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
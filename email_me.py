#!/usr/bin/env python3

import compose_message
import smtplib
import socket

from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders

""" info on where to message to and from """
fromaddr = '*****'
password = '*****'
toaddr = '*****'

""" set up the message, get the to, from and subject input """
now = datetime.now()
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Your morning update for %s" % (now.strftime('%m/%d/%Y'))


""" here build up the body of the text """
body = compose_message.create_text_body()
msg.attach(MIMEText(body, 'plain'))

""" here add the graphs of stock prices to the message """
""" go to compose_message.py to change the stocks of interest"""
msg = compose_message.create_stock_graphs(msg)

""" look at the docs here, see if you can change the 'plain' to alter the format """	


""" connect to the gmail server, send the email """
""" note you've gotta change the email account's
	settings to allow unsecure access """
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

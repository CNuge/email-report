#!/usr/bin/env python3

import message.compose_message as compose_message

import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

""" info on where to message to and from """
fromaddr = '*****'	# CHANGE TO: the email address the message will send from
password = '*****'	# CHANGE TO: the password for fromaddr
toaddr = '*****'	# CHANGE TO: the email address the message will be sent to

""" set up the message"""
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
now = datetime.now() #optional, can remove if you change the subject line below
msg['Subject'] = "Your report for %s" % (now.strftime('%m/%d/%Y')) #change subject line here!

""" here build up the body of the text """
body = compose_message.create_text_body() #this calls compose_message to build the report 
msg.attach(MIMEText(body, 'plain')) #note this is plan text

# advanced: you could attach images, files or other formatted data here in addition to just plain text strings!
# have a look at the docs, this may take some extra work!:
# https://docs.python.org/3/library/email.mime.html

""" connect to the gmail server, send the email 
	note: change the email account's settings to allow unsecure access 
	I would recommend a new dummy email account to send the report from!"""
server = smtplib.SMTP('smtp.gmail.com', 587) #this is gmail specific, for yahoo it would be: (smtp.mail.yahoo.com, 587)
server.starttls()
server.login(fromaddr, password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
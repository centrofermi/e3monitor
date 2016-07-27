#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:00:00 2016

@author: Fabrizio Coccetti (fabrizio.coccetti@centrofermi.it) [www.fc8.net]
Send EEE email report via Gmail
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import locale
import ConfigParser
import logging
import logging.config
from datetime import datetime
from e3monitor.config.__files_server__ import (logConfigFile,
                                               emailConfigFile)

# Set up logging
logging.config.fileConfig(logConfigFile)
logger = logging.getLogger('full')
logger.info('Started')
logger = logging.getLogger('plain')

# Set locale to Italian
locale.setlocale(locale.LC_ALL, 'it_IT')

# Reading Email Config File
logger.info('Reading ' + emailConfigFile)
parser = ConfigParser.ConfigParser()
parser.read(emailConfigFile)
smtpServer = parser.get('gmail','smtpServer')
smtpPort = parser.get('gmail','smtpPort')
emailFrom = parser.get('gmail','emailFrom')
emailTo = parser.get('gmail','emailTo')
passwd = parser.get('gmail','passwd')

# Create message container - the correct MIME type is multipart/alternative.
today = datetime.today()
todayStr = today.strftime("%a %d %B %Y")
msg = MIMEMultipart('alternative')
msg['Subject'] = "Report giornaliero di EEE - Situazione alle ore 8:00 di " + todayStr
msg['From'] = emailFrom
msg['To'] = emailTo

# Create the body of the message (a plain-text and an HTML version).
text = "The message is in html format. It looks like your client does not support it"
html = """\
<html>
  <head></head>
  <body>
Shift Report di """ + todayStr + \
"""
<br />
***************************<br />
<B>NEVER REPLY</B> TO THIS LIST!!<br />
Please reply only to the sender and runcoord@centrofermi.it<br />
****************************<br />

  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Sending message
logger.info('Sending message via Gmail')
s = smtplib.SMTP(smtpServer + ":" + smtpPort)
s.starttls()
s.login(emailFrom, passwd)
s.sendmail(emailFrom, emailTo, msg.as_string())
s.quit()

logger.info('Finished')


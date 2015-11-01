#
# Neil Trimboy 2011
# Assume Pyhton 2.7.x
#

#from struct import pack
#import time
import sys
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.mime.text import MIMEText
from email import Encoders
import os
#import shutil

# Import our own stuff

import email_settings

# Source
# http://kutuma.blogspot.com/2007/08/sending-emails-via-gmail-with-python.html
# plus mod for optional attachement from same blog entry
def mail(to, subject, text, attach=None):
   msg = MIMEMultipart()

   msg['From'] = email_settings.email_from_addr
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))
  
   if attach:
       print attach
       print os.path.normpath(attach)
       fp = open(attach, 'r')
       msg.attach(MIMEText(fp.read()))# Put the attachment in line also
       fp.close()

       part = MIMEBase('application', 'octet-stream')
       part.set_payload(open(attach, 'rb').read())
       Encoders.encode_base64(part)
       part.add_header('Content-Disposition',
               'attachment; filename="%s"' % os.path.basename(attach))
       msg.attach(part)
   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(email_settings.email_from_addr, email_settings.gmail_pwd)
   mailServer.sendmail(email_settings.email_from_addr, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()
   
   

 

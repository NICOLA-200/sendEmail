import os

from email.message import EmailMessage
import ssl

import smtplib


email_sender  = 'fatepepe66@gmail.com'
email_password = 'jywv mdld nztk myvy'
email_receiver = 'nsengiyumvanicolas74@gmail.com' 


subject = 'check out my new video'

body = """
I've  just published a new video on Youtube
"""


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)
 
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
     smtp.login(email_sender,email_password)

     smtp.sendmail(email_sender, email_receiver, em.as_string())















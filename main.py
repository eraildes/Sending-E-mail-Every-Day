import yagmail
import os
import time
from datetime import datetime as dt
from datetime import timezone, timedelta

sender = 'eraildesds@gmail.com'

receiver = 'mxphtrthb@firste.ml'
subject = 'This is the subject'

content = """"
here is the content of the e-mail
"""
while True:
  now = dt.now() - timedelta(hours=3)
  if now.hour == 12 and now.minute == 43:
    yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
    yag.send(to=receiver, subject=subject, contents=content)
    print("E-mail Sent!")
    time.sleep(60)
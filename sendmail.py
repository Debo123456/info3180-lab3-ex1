import smtplib
from_addr = 'yourusername@gmail.com'
to_addr = 'danieldawson496@gmail.com'

from_name = 'Daniel Dawson'
to_name = 'Daniel Dawson'
subject = 'Test'
msg = 'This is a test'

message = """From: {0} <{1}>
To: {2} <{3}> 


Subject: {4}
{5}
"""
message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)
# Credentials (if needed)
username = 'secursally@gmail.com'
password = 'password'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit() 
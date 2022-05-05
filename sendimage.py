
from http import server
import smtplib
from email.message import EmailMessage
import imghdr
from email import message

 
message = EmailMessage()
email_subject = "Email alert"
sender_email_address = "wangchunbo551999@gmail.com"
receiver_emaill_address = "haudao111@gmail.com"
email_smtp ="smtp.gmail.com"
email_password = "poahlxihwconiltp"

with open('download.jpg', 'rb' ) as f:
     image_data = f.read()
   
message.set_content("CR7")

message['Subject'] = email_subject
message['From'] = sender_email_address
message['to'] = receiver_emaill_address

message.add_attachment(image_data, maintype = 'image', subtype = imghdr.what(None, image_data))

server = smtplib.SMTP(email_smtp, 587)
server.ehlo()
server.starttls()

server.login(sender_email_address, email_password)
server.send_message(message)
server.quit()
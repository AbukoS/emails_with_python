import os
import smtplib
from email.message import EmailMessage


msg = EmailMessage()

msg['From'] = 'buteksonline@gmail.com'
msg['To'] = 'sidney.abuko@gmail.com'
msg['Subject'] = 'How about dinner tonight ??'

sid = "Sidney Abuko Omuteku"
image_url = "https://lh3.googleusercontent.com/proxy/a7acaE1bbTRLUcTo5DhAI5YQx6ObrivKcR6ThNj-0amPiTfQgUj0vBA2rolD6di9Gh2EZyvMdpT3TbNqDPu0PVjieeBpF7odsZBcApXprrYHHjfBaU9K"
message = f"""
    
    <div style="text-align:center; width:70%; margin: 2em auto; border: 1px solid gray; border-radius: 10px;">
        <h1 style="width:100%; margin:2em 0 0 0;">{sid}</h1>
        <hr/ style="margin: 2em auto;">
        <img  src={image_url} style="width:100%; height:300px; padding:10px; alt="Image"/>
        <h5>Product title</h5>
        <hr/>
        <p>
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
        </p>
        <hr/>
        <button style="display: block; background-color:gray; width: 90%; margin: 2em auto; height: 45px; color: white;border-radius:20px; outline:none; border:none; text-transform: uppercase;" >Add to cart</button>
    </div>

"""

msg.add_alternative(message, 'html')

# smtp = smtplib.SMTP_SSL(host='smtp.gmail.com', port=443)
# smtp.login('host_user', 'host_password/app_password if gmail')
# smtp.send_message(msg)

smtp = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp.starttls()
smtp.login('host_user', 'host_password/app_password if gmail')
smtp.send_message(msg)

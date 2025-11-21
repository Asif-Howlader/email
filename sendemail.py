import smtplib
import ssl
import time
import sys
from email.message import EmailMessage

fromaddr = ''
toaddr  = input("Enter recipient's email address: ")
password = 'xawj kctq pbvk obzb' # NOT your normal Gmail password

msg = EmailMessage()
msg["Subject"] = input("Enter the subject line: ")
msg["From"] = fromaddr
msg["To"] = toaddr
msg.set_content(input("Enter the body of the email: "))

context = ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls(context=context)
    server.login(fromaddr, password)
    server.send_message(msg)

for i in range(0, 101):
    bar = '=' * (i // 2)
    sys.stdout.write(f'\rEmail Sending [{bar:<50}] {i}%')
    sys.stdout.flush()
    time.sleep(0.05)

print()  # move to new line after completion
print("Done!")

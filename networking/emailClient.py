import smtplib
from email.mime.text import MIMEText  # We use this to build our email body

body = "This is a test email. How are you?"

msg = MIMEText(body)
msg['From'] = "hasanumutuzunoz@gmail.com"
msg['To'] = "hasanumutuzunoz@gmail.com"
msg['Subject'] = "Hello"

# Open a smtp server connection
server = smtplib.SMTP('smtp.gmail.com',587)

# Enable TLS connection
server.starttls()

#Login with username and password
server.login("codetest987654321@gmail.com", "codetester92837")

# Sent the message
server.send_message(msg)

print("Mail Sent")

server.quit()
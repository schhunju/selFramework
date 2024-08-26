import smtplib
from email.mime.text import MIMEText

try:
    # Create the email
    msg = MIMEText('Hello!..This is the body of the email.')
    msg['Subject'] = 'Subject of the Email'
    msg['From'] = 'sapkotaarchana6@gmail.com'
    msg['To'] = 'arkanasapkota6@gmail.com'

    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # Upgrade the connection to a secure encrypted SSL/TLS connection
    server.starttls()

    # Login to the server
    server.login('sapkotaarchana6@gmail.com', 'wqog vgcj wvdz xidv')

    # Send the email
    server.send_message(msg)


except smtplib.SMTPException as e:
    print(f"An error occurred: {e}")

finally:
    server.quit()

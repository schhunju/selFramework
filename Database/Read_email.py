import imaplib
import email
from email.header import decode_header
import yaml

# Load credentials from the YAML file
with open(r"C:\\Users\\ArchanaSapkota\\PycharmProjects\\selFramework\\Database\\config.yaml", "r") as file:
    config = yaml.safe_load(file)

email_address = config['email_credentials']['email']
password = config['email_credentials']['password']

mail = imaplib.IMAP4_SSL("imap.gmail.com")  # Connecting to the Gmail IMAP server

mail.login(email_address, password)     # Log in to the email account

mail.select("inbox")        # Select the mailbox you want to check

status, messages = mail.search(None, "ALL")     # Searching for all emails in the inbox

email_ids = messages[0].split()     # Converting the result to a list of email IDs

latest_email_id = email_ids[-1]     # Fetching the latest email (change the index to fetch different emails)

status, msg_data = mail.fetch(latest_email_id, "(RFC822)")      # Fetching the email by ID

# Extracting email message
for response_part in msg_data:
    if isinstance(response_part, tuple):
        msg = email.message_from_bytes(response_part[1])

        # Decoding email subject
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else "utf-8")

        # Printing subject
        print("Subject:", subject)

        # Decoding sender's email address
        from_ = msg.get("From")
        print("From:", from_)

        # If the email message is multipart
        if msg.is_multipart():
            for part in msg.walk():
                # Get the content type of the email
                content_type = part.get_content_type()
                if content_type == 'text/plain':
                    # Extract plain text
                    plain_text_body = part.get_payload(decode=True).decode()
                    break  # We found the plain text part, so break out of the loop
            if plain_text_body:
                print("Body:", plain_text_body)
            else:
                print("No plain text part found.")
        else:
            # If the email message isn't multipart, it might be plain text
            if msg.get_content_type() == 'text/plain':
                body = msg.get_payload(decode=True).decode()
                print("Body:", body)
            else:
                print("No plain text part found.")

# Log out after reading emails
mail.logout()
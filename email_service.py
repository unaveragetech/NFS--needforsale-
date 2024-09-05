# email_service.py
import smtplib
import imaplib
import email
from email.mime.text import MIMEText

# Function to send an email
def send_email(sender, password, recipient, subject, body):
    msg = MIMEText(body, 'html')  # Create an HTML email message
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

    try:
        with smtplib.SMTP_SSL('smtp.mail.com', 465) as smtp:
            smtp.login(sender, password)  # Log into mail server
            smtp.send_message(msg)        # Send email
            print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {str(e)}")

# Function to read inbox messages
def read_inbox(email_user, email_pass):
    try:
        with imaplib.IMAP4_SSL('imap.mail.com') as mail:
            mail.login(email_user, email_pass)  # Log into mail server
            mail.select('inbox')                # Select inbox
            result, data = mail.search(None, 'ALL')  # Fetch all emails
            for num in data[0].split():
                result, data = mail.fetch(num, '(RFC822)')
                msg = email.message_from_bytes(data[0][1])
                print(f"Subject: {msg['subject']}")
    except Exception as e:
        print(f"Failed to read inbox: {str(e)}")

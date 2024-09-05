# scheduler.py
import threading
import time
from email_service import send_email

# Function to send emails at a given interval (in seconds)
def send_scheduled_email(interval, sender, password, recipient, subject, body):
    while True:
        send_email(sender, password, recipient, subject, body)
        time.sleep(interval)

# Start email campaign in the background
def start_email_campaign(sender, password, recipient, subject, body, interval):
    threading.Thread(target=send_scheduled_email, args=(interval, sender, password, recipient, subject, body)).start()

# Example of scheduling an email campaign
if __name__ == "__main__":
    sender = "youremail@mail.com"
    password = "yourpassword"
    recipient = "customer@example.com"
    subject = "Weekend Sale"
    body = "Save 50% this weekend only!"
    interval = 86400  # Send every 24 hours

    start_email_campaign(sender, password, recipient, subject, body, interval)

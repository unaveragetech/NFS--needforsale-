# main.py
from email_service import send_email
from ad_generation import generate_ad
from scheduler import start_email_campaign
from analytics import log_email
from contact_manager import load_contacts
from datetime import datetime

# Main function to send ad campaign to all contacts
def start_ad_campaign(sender, password, subject, content, contacts, interval):
    for contact in contacts:
        ad_body = generate_ad(subject, content, (datetime.now().strftime('%Y-%m-%d')))
        send_email(sender, password, contact['email'], subject, ad_body)
        log_email(contact['email'], subject)

    # Start scheduled campaign to keep sending the same ad at regular intervals
    for contact in contacts:
        start_email_campaign(sender, password, contact['email'], subject, content, interval)

# Example usage
if __name__ == "__main__":
    sender = "youremail@mail.com"
    password = "yourpassword"
    subject = "Weekend Sale!"
    content = "Save 50% this weekend only!"
    contacts = load_contacts('contacts.csv')
    interval = 86400  # Every 24 hours

    start_ad_campaign(sender, password, subject, content, contacts, interval)

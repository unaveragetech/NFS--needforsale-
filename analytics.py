# analytics.py
import csv
from datetime import datetime
import os

# Log sent email to CSV
def log_email(sent_to, subject):
    file_exists = os.path.isfile('email_log.csv')
    with open('email_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Timestamp', 'Recipient', 'Subject'])  # Write header if file is new
        writer.writerow([datetime.now(), sent_to, subject])

# Example usage
if __name__ == "__main__":
    log_email("customer@example.com", "Weekend Sale!")

# contact_manager.py
import csv

# Function to load contacts from a CSV file
def load_contacts(file_path):
    contacts = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            contacts.append({'name': row[0], 'email': row[1]})
    return contacts

# Function to save contacts to a CSV file
def save_contacts(file_path, contacts):
    with open(file_path, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for contact in contacts:
            writer.writerow([contact['name'], contact['email']])

# Example usage
if __name__ == "__main__":
    contacts = load_contacts('contacts.csv')
    save_contacts('contacts.csv', [{'name': 'John Doe', 'email': 'john@example.com'}])

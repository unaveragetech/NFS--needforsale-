import os
import csv
import tkinter as tk
from tkinter import messagebox

# Define the folder and file paths
folder_name = "user_data"
csv_file = os.path.join(folder_name, "contacts.csv")

# Create the folder if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Function to save the user data to CSV
def save_data(name, email):
    # Check if name and email fields are filled
    if not name or not email:
        messagebox.showwarning("Input Error", "Please enter both Name and Email")
        return
    
    # Check if email is valid (basic validation)
    if "@" not in email or "." not in email:
        messagebox.showwarning("Input Error", "Please enter a valid Email")
        return
    
    # Append the new data to the CSV file
    file_exists = os.path.isfile(csv_file)
    
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write headers only if file doesn't exist
        if not file_exists:
            writer.writerow(['Name', 'Email'])
        
        writer.writerow([name, email])
    
    messagebox.showinfo("Success", "Data saved successfully!")
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Function to handle the "Submit" button click
def submit_action():
    name = entry_name.get()
    email = entry_email.get()
    save_data(name, email)

# GUI Setup
root = tk.Tk()
root.title("User Info Collector")

# Define and place the labels and entries
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=1, column=0, padx=10, pady=10)

entry_email = tk.Entry(root, width=30)
entry_email.grid(row=1, column=1, padx=10, pady=10)

# Define and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit_action)
submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI main loop
root.mainloop()

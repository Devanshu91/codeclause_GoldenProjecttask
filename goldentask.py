# codeclause_GoldenProjecttask

import tkinter as tk
from tkinter import messagebox

def send_mail():
    recipient = recipient_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)

    # Add your code here to send the mail using your preferred email library or API

    messagebox.showinfo("Mail Sent", "Mail has been sent successfully!")

# Create the main application window
root = tk.Tk()
root.title("Mail Application")

# Labels
tk.Label(root, text="Recipient:").pack()
tk.Label(root, text="Subject:").pack()
tk.Label(root, text="Message:").pack()

# Entry fields
recipient_entry = tk.Entry(root)
recipient_entry.pack()
subject_entry = tk.Entry(root)
subject_entry.pack()

# Text area for message
message_text = tk.Text(root, width=40, height=10)
message_text.pack()

# Send button
send_button = tk.Button(root, text="Send Mail", command=send_mail)
send_button.pack()

# Run the main event loop
root.mainloop()

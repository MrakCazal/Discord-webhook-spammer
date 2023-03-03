import requests
import tkinter as tk
from tkinter import messagebox

def send_message():
    # Abrufen der Eingabe von Nutzer
    webhook_url = webhook_url_entry.get()
    message = message_entry.get()
    count = count_var.get()

    # Verwenden einer Session für Keep-Alive
    session = requests.Session()

    # Senden der Nachrichten
    for i in range(count):
        response = session.post(webhook_url, json={'content': message})
        print(f'Sent message {i+1}/{count} with status {response.status_code}')

    # Zeigen einer Bestätigungsnachricht
    messagebox.showinfo("Information", f"All messages sent to {webhook_url}")

# Erstellen der Hauptfenster
root = tk.Tk()
root.title("Discord Webhook Spammer")

# Erstellen der Label und Entry-Felder
webhook_url_label = tk.Label(root, text="Webhook URL:")
webhook_url_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
webhook_url_entry = tk.Entry(root, width=50)
webhook_url_entry.grid(row=0, column=1, padx=5, pady=5)

message_label = tk.Label(root, text="Message:")
message_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
message_entry = tk.Entry(root, width=50)
message_entry.grid(row=1, column=1, padx=5, pady=5)

count_label = tk.Label(root, text="Number of messages:")
count_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
count_var = tk.IntVar()
count_entry = tk.Entry(root, width=10, textvariable=count_var)
count_entry.grid(row=2, column=1, padx=5, pady=5)

# Erstellen der Senden-Schaltfläche
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Erstellen des Contact-Me-Buttons
def open_link():
    import webbrowser
    webbrowser.open("https://solo.to/mrak")

contact_me_button = tk.Button(root, text="Contact Me", command=open_link)
contact_me_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
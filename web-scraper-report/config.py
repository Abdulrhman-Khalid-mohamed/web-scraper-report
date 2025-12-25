import os

URLS = ["https://coinmarketcap.com/"]

OUTPUT_FOLDER = "outputs"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

EMAIL_ENABLED = False
EMAIL_SENDER = "your_email@example.com"
EMAIL_RECEIVER = "receiver_email@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_PASSWORD = "your_email_password"

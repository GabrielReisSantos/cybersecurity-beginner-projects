import re
import os
import smtplib
import requests
from datetime import datetime
from email.message import EmailMessage

LOG_FILE = input("Enter the name of the log file to analyze: ").strip()

ALERT_LOG = "alerts.log"

# Email settings (update with your actual info or environment variables)
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # Use Gmail App Password

# Discord webhook (update with your actual webhook)
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/"

# Patterns to detect suspicious activity
patterns = {
    "Failed SSH login": r"Failed password for.*from (\d+\.\d+\.\d+\.\d+)",
    "Root login": r"session opened for user root",
    "Invalid user": r"Invalid user (\w+) from (\d+\.\d+\.\d+\.\d+)",
    "Sudo use": r"sudo: .*",
    "Suspicious script run": r"COMMAND=.*\.sh"
}

def send_email_alert(subject, body):
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("[✔] Email alert sent.")
    except Exception as e:
        print(f"[!] Failed to send email: {e}")

def send_discord_alert(message):
    payload = {"content": f"🚨 Log Alert: {message}"}
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        if response.status_code == 204:
            print("[✔] Discord alert sent.")
        else:
            print(f"[!] Failed to send Discord alert: {response.status_code}")
    except Exception as e:
        print(f"[!] Discord error: {e}")

def analyze_logs(log_file):
    alerts = []
    if not os.path.exists(log_file):
        print(f"[!] Log file not found: {log_file}")
        return

    with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    for line in lines:
        for alert_type, pattern in patterns.items():
            if re.search(pattern, line):
                timestamp = datetime.now()
                log_entry = f"[{timestamp}] {alert_type}: {line.strip()}"
                print(log_entry)
                alerts.append(log_entry)
                send_email_alert(f"[Log Alert] {alert_type}", log_entry)
                send_discord_alert(log_entry)

    if alerts:
        with open(ALERT_LOG, "a") as alert_file:
            for alert in alerts:
                alert_file.write(alert + "\n")
    else:
        print("[✓] No suspicious activity detected.")

if __name__ == "__main__":
    print("🔍 Running Extended Log Analyzer...")
    analyze_logs(LOG_FILE)

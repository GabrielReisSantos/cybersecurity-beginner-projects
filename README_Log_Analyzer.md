# Log Analyzer with Alerts

A real-world style Python tool that analyzes system logs for security alerts and sends notifications via **Email** and **Discord**.

---

## Features

- Detects:
  - Failed SSH logins
  - Root access
  - Invalid login attempts
  - `sudo` command usage
  - Suspicious `.sh` script execution
- Sends alerts via:
  - Email (Gmail App Passwords)
  - Discord Webhook
- Appends all alerts to `alerts.log`

---

## Setup

### 1. Install dependencies
```bash
pip install requests
```

### 2. Configure Email and Webhook
Edit the `log_analyzer.py` file:
- Replace `EMAIL_ADDRESS`, `EMAIL_PASSWORD` (Gmail App Password)
- Replace `DISCORD_WEBHOOK_URL` with your webhook URL

---

## Run the Tool

```bash
python3 log_analyzer.py
```

---

## Sample Log for Testing

Use `test_auth.log`:
```bash
LOG_FILE = "test_auth.log"
```

You can simulate activity like:
```bash
echo "Apr 11 16:00:00 ubuntu sudo: user : TTY=pts/1 ; USER=root ; COMMAND=/bin/bash script.sh" >> test_auth.log
```

---

## Disclaimer

This tool is for **educational use only**. Don't monitor or scan systems without permission.

---

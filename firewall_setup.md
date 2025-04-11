# Firewall Setup with UFW

This guide simulates real-world firewall configurations using `ufw` (Uncomplicated Firewall), great for testing and learning on virtual machine.

---

## Prerequisites

- Ubuntu/Debian-based system (use VM or Docker on macOS if needed)
- `ufw` installed:
```bash
sudo apt update
sudo apt install ufw
```

---

## Real-World Rules & Scenarios

### 1. Default Deny Policy
```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

---

### 2. Allow Web Server (HTTP/HTTPS)
```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

---

### 3. Allow SSH Only From Your IP
Replace with your real IP:
```bash
sudo ufw allow from 203.0.113.25 to any port 22 proto tcp
sudo ufw deny 22/tcp
```

---

### 4. Block Known Malicious Ports
```bash
sudo ufw deny 23/tcp  # Telnet
sudo ufw deny 135,137,138,139,445/tcp
```

---

### 5. Rate Limit SSH (Anti-Brute Force)
```bash
sudo ufw limit 22/tcp
```

---

### 6. Simulate Local-Only Services
Imagine a database on port 5432:
```bash
sudo ufw allow in on lo to any port 5432
```

---

### 7. Enable Logging
```bash
sudo ufw logging on
```

---

### 8. View Current Rules
```bash
sudo ufw status verbose
sudo ufw show added
```

---

## Test with curl, nmap, telnet (optional)
```bash
nmap localhost
telnet localhost 80
```

⚠️ Always test on VMs, never on production or networks without permission.

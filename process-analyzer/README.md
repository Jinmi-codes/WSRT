# 🧠 Process Analyzer (Part of WSRT)

A lightweight Python tool that analyzes running Windows processes to detect anomalies, such as:
- High CPU usage
- Multiple process instances
- Suspicious or rare process names

This is part of the **Windows System Recon Tools (WSRT)** series.

---

## 🚀 How It Works

The script uses PowerShell to fetch all running processes, then:
- Counts instances of each process name.
- Flags suspiciously named processes.
- Flags processes consuming abnormally high CPU.

---

## 📂 Output

- `processes.log` — raw running process info
- `events.log` — structured analysis report

---

## 🛠️ Usage

```bash
python analyzer.py
```

This is still a work in progress!!
Argparse, error handling, and enhanced detection are planned. (For when I'm less headachey..)
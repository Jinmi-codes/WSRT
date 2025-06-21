# 🛡️ Windows System Recon Tools (WSRT)

A modular toolkit for Windows system analysis, inspection, and security context building.  
Built with **Python** and **PowerShell** during my learning process.

---

## 🧰 Tools Included

### 1. 🔍 IP Blacklist Checker (v1.3)
Scans active TCP connections and compares IPs to a simulated blacklist.

- 📁 Path: `ip-blacklist-checker/`
- 🛠️ Tech: Python, PowerShell, `subprocess`, `argparse`
- 📄 [Tool README](ip-blacklist-checker/README.md)

---

### 2. 🧪 Process Analyzer *(Coming Soon)*
Parses active system processes, flags suspicious behavior, and exports logs.

### 3. 🚦 Startup Inspector *(Planned)*
Analyzes system startup entries and identifies insecure or unnecessary items.

---

## 🚀 Getting Started

Clone the repository:
```bash
git clone https://github.com/Jinmi-codes/WSRT.git
```
Quick Example:
```bash
cd WSRT/ip-blacklist-checker
python main.py --save output --alerts alerts
```

---

## 📦 Requirements

- Windows OS
- Python 3.8+
- PowerShell (in system PATH)


Install optional packages:
```bash
none yet
```

---

## 📄 License

MIT License.  
See [LICENSE](LICENSE) file for details.

---

## 👨🏽‍💻 Author

**Jinmi-Codes (Koji)**  
Security+ Certified | I LOVE PEANUTS AND I AM SEVERELY SLEEP DEPRIVED.
🔗 [GitHub @Jinmi-codes](https://github.com/Jinmi-codes)

---

> This is a personal project to sharpen my skills in systems, scripting, and security tooling.
> I made this solely to showcase my understanding of various windows concepts through implementation with python and other scripting languages.
> I'm so locked in rn!

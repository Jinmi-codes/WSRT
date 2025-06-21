# 🛡️ Windows System Recon Tools (WSRT)

A modular toolkit for Windows system analysis, inspection, and security context building.  
Built with **Python** and **PowerShell** during my learning process.

---

## 🧰 Tools Included

### 1. 🔍 IP Blacklist Checker (v1.1)
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


## 🤝 Contributing

Got ideas for new tools or improvements?

1. Fork the repo
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-tool
   ```
3. Commit and push your changes:
   ```bash
   git commit -m "Add new WSRT tool"
   git push origin feature/your-tool
   ```
4. Submit a pull request with details

---

## 📄 License

MIT License.  
See [LICENSE](LICENSE) file for details.

---

## 👨🏽‍💻 Author

**Jinmi-Codes (Koji)**  
Security+ Certified | LOVES PEANUT BUTTER
🔗 [GitHub @Jinmi-codes](https://github.com/Jinmi-codes)

---

> This is a personal project to sharpen my skills in systems, scripting, and security tooling.  
> The goal is **tools that work**

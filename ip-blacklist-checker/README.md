## 🛠 v1.3 - IP-Blacklist-Checker.
 >Uses PowerShell subprocess to collect current TCP connections and checks them against a blacklist of IP addresses. 
 >The script logs all remote IPs from active connections, filters out invalid or irrelevant entries, and compares them to a provided blacklist file.
 >If any blacklisted IPs are found, it flags them and prints a warning for each one. (CANNOT TAKE ACTION/TERMINATE CONNECTIONS.) yet..
>Added CLI capabilities in v1.3

## ⚙️ How to Use

### 📥 Step 1: Clone the Repository

```bash
git clone https://github.com/Jinmi-codes/WSRT.git
cd WSRT/ip-blacklist-checker
```

---

### 🚀 Step 2: Run the Script

```bash
python main.py --save <output_file_name> --alerts <alerts_file_name>
```

#### 🔹 Example:
```bash
python main.py --save tcp_output --alerts flagged_ips
```

- `--save` ➤ The name of the file to store all active TCP connection IPs (e.g. `tcp_output.log`)
- `--alerts` ➤ The name of the file to store malicious/suspicious IPs found in the scan (e.g. `flagged_ips.log`)

---

### 📄 Output Files

- ✅ `tcp_output.log` — Raw IP addresses from `Get-NetTcpConnection`
- ⚠️ `flagged_ips.log` — Only IPs flagged as **malicious**

---

### 📝 Notes

- Script uses PowerShell’s `Get-NetTcpConnection` — works only on **Windows**.
- IP reputation is simulated for now. I will implement live api checking...eventually.
- I made this to solidify and show my understanding of file creation and use of Subprocess.
---

### 🧪 Sample Output
```
The following TCP connections are active as of 04:21:58 PM:
-------------------
216.58.223.228
34.107.243.93
-------------------
[!] 216.58.223.228 is malicious !!
34.107.243.93 is clean
```

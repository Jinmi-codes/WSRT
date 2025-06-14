##  v1 - TCP Connection Blacklist Checker.
 >Uses PowerShell subprocess to collect current TCP connections and checks them against a blacklist of IP addresses. 
 >The script logs all remote IPs from active connections, filters out invalid or irrelevant entries, and compares them to a provided blacklist file.
 >If any blacklisted IPs are found, it flags them and prints a warning for each one. (CANNOT TAKE ACTION/TERMINATE CONNECTIONS.) yet..

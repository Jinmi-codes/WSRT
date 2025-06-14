import subprocess
import re

#not written by me, cuz who tf understands regex?
def is_ip(line):
    return re.match(r"^\d{1,3}(\.\d{1,3}){3}$", line)
#not written by me.


raw_iP = subprocess.run(["powershell","Get-NetTcpConnection | select-object RemoteAddress"], capture_output=True, text=True)

with open("connections.log", "w") as open_connections:
    open_connections.write(raw_iP.stdout)


clean_iP=[]
with open("connections.log", "r") as open_connections:
    for line in open_connections:
        if is_ip(line.strip()) and line.strip() != "0.0.0.0":
            clean_iP.append(line.strip())


clean_iP = set(clean_iP) # removing duplicates, top 10 greatest feats of engineering
clean_iP = list(clean_iP)


#simulated reputation because I don't understand API's.....YET!
reputation = {
    'malicious':['138.61.242.156', '30.249.33.38', '229.246.212.170', '252.254.234.227', '166.148.73.141', '35.186.227.140', '52.123.128.14', '135.236.136.109'],
    'clean':['53.71.59.132', '0.225.189.60', '69.222.143.41', '76.130.201.234', '236.227.243.166'],
    'safe':[ '93.95.240.117', '204.102.227.226', '226.195.118.160', '154.185.126.64', '184.248.19.65', '75.193.17.1', '5.212.228.83', '107.70.83.102', '218.192.207.125', '140.148.155.93']
}

for ip in clean_iP:
    if ip in reputation['clean']:
        print(f"{ip} is clean")
    elif ip in reputation['malicious']:
        print(f"⚠ { ip} is malicious !!")
        with open("malicious_Ip.txt", "w") as malicious:
            malicious.writelines(ip)
    elif ip in reputation['safe']:
         print(f"{ip} is safe")


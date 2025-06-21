import subprocess
import argparse
from datetime import datetime
import re
invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']

#not written by me, cuz who tf understands regex?
def is_ip(line):
    return re.match(r"^\d{1,3}(\.\d{1,3}){3}$", line)
#not written by me.

parse = argparse.ArgumentParser(description="Command Line tool that scans open TCP conections and provides feedback.")
parse.add_argument('--save', '-s', help="Specify file name for storing active connections.", required=True)
parse.add_argument('--alerts', '-a', help="Specify file name for storing alerts.", required=True)
args = parse.parse_args()

tcp_file = args.save
tcp_file = tcp_file.strip()

alert_file = args.alerts
alert_file = alert_file.strip()


def getTime():
    time= datetime.now().time().strftime("%I:%M:%S %p")
    strTime = str(time)
    return strTime

time = getTime()
    

raw_iP = subprocess.run(["powershell","Get-NetTcpConnection | select-object RemoteAddress"], capture_output=True, text=True)

if not any(char in invalid_chars for char in tcp_file) and not any(char in invalid_chars for char in alert_file):
       
    try :
        with open(f"{tcp_file}.log", "w") as open_connections:
            open_connections.write(raw_iP.stdout)


        clean_iP=[]
        with open(f"{tcp_file}.log", "r") as open_connections:
            for line in open_connections:
                if is_ip(line.strip()) and line.strip() != "0.0.0.0":
                    clean_iP.append(line.strip())


        clean_iP = set(clean_iP) # removing duplicates, top 10 greatest feats of engineering
        clean_iP = list(clean_iP)


        #simulated reputation because I don't understand API's.....YET!
        reputation = {
            'malicious':['216.58.223.228', '34.107.243.93', '229.246.212.170', '252.254.234.227', '2.18.190.148', '35.186.227.140', '52.123.128.14', '135.236.136.109'],
            'clean':['53.71.59.132', '0.225.189.60', '69.222.143.41', '76.130.201.234', '236.227.243.166'],
            'safe':[ '93.95.240.117', '204.102.227.226', '226.195.118.160', '154.185.126.64', '184.248.19.65', '75.193.17.1', '5.212.228.83', '107.70.83.102', '218.192.207.125', '140.148.155.93']
        }



        print(f"The following TCP connections are active as of {time} :\n-------------------")
        for ip in clean_iP:
            print(ip)
        print("-------------------")

        mal_count = 0

        with open(f"{alert_file}.log", "w") as malicious:
            malicious.write(f"Time stamp: {time} \n")
            for ip in clean_iP:
                if ip in reputation['clean']:
                    print(f"{ip} is clean")
                elif ip in reputation['malicious']:
                    print(f"[!] { ip} is malicious !!")
                    malicious.write(f"{ip} \n")
                elif ip in reputation['safe']:
                    print(f"{ip} is safe")
    except FileNotFoundError:
        print("[!] Inavlid File.")
        pass
else:
    print("[!] Inavlid File name.")
    pass
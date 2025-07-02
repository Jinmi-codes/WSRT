import re
import subprocess
import argparse
from collections import Counter
from datetime import datetime



#CLI functionality
argparser = argparse.ArgumentParser(description="A Command line tool that analyzes running processes and returns certain metrics.")
argparser.add_argument('--save', '-s', help="Specify where the raw process information is to be saved, without a specified extension. Default is .log", required=True)
argparser.add_argument('--log', '-l', help="Specify where the output of the program is to be saved, without a specified extension. Default is .log", required=True)
args = argparser.parse_args()

save_file = args.save
events_file = args.log

date= datetime.now()


suspicious_names = [
    
    "svhost", "svch0st", "expl0rer", "taskmgrs", "system32", "lsaas",
    "meterpreter", "njrat", "xrat", "darkcomet", "keylogger", "rattool",
    "backdoor", "crypter", "psexec", "reverse_shell", "shell",
    "update", "temp", "winupdate", "browserupdate", "servicehost",
    "a1b2c3", "qwopfdks", "zxcasd", "lkjhgfd", "random123.",
    "mimikatz", "ncat", "netcat", "nmap", "whoami", "powershell"
]


processes = subprocess.run(["Powershell","Get-Process | Select-Object ProcessName, Id, CPU"], capture_output=True, text=True)

#initializing lists.
processed = []
prcs = []
process_name = []
cpu_usage = []
invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']

if not any(char in invalid_chars for char in events_file) and not any(char in invalid_chars for char in save_file):
       
   try:
        print("Windows System Recon Tools - Process Analyzer ")
        print(f"[Analysis was made on {date.date()}]" )
        print("\n")
        #file creation for running processes.
        with open(f"{save_file}.log", 'w') as logged_processes:
            logged_processes.write(processes.stdout)
            

            
        with open(f"{save_file}.log", 'r') as logged_processes:
            
            for line in logged_processes:
                if len(line.strip().split()) == 3:
                    prcs.append(line.strip().split())
        
        #creating local and cleaner version(a dictionary) of processes log.       
        for line in prcs:
            processed.append({line[0]:[line[1],line[2]]})
            


        processed.pop(1)
        processed.pop(2)

            
        #Collecting process names
        for dict in processed:
            for key in dict:
                process_name.append(key)
                
                
                
        counter = Counter(process_name)

        #main logic

        print("Multiple Instances: ")
        print("--------------------------")

        with open(f"{events_file}.log", 'w') as events:
            events.write("Multiple Instances: \n")
            for key, count in counter.items():
                if count >= 2:
                    print(f"[!] {key} is running {count} instances.")
                    events.write(f"[!] {key} is running {count} instances.\n")
            print(" \n")
            events.write(" \n")
            print("Suspicious Processes: ")
            events.write("Suspicious Processes: \n")
            print("--------------------------")
            for proc_name in set(process_name):
                if proc_name in suspicious_names:
                    print(f"[!] {proc_name} is suspicious! ")
                    events.write(f"[!] {proc_name} is suspicious! \n")
            print(" \n")
            events.write(" \n")

            print("Abnormal Cpu Usage:")
            events.write("Abnormal Cpu Usage: \n")
            print("--------------------------")

            for dict in processed:
                for key in dict:
                    if not dict[key][1].isalpha() and not dict[key][0].isalpha():
                        if float(dict[key][1]) > 50:
                            print(f"[!] PID[{dict[key][0]}] Process {key} is using {dict[key][1]}")
                            events.write(f"[!] PID[{dict[key][0]}] Process {key} is using {dict[key][1]}\n")
                            



            print("--------------------------")
            
   except FileExistsError:
       print("hold")
else:
    print("[!] Invalid file name!")
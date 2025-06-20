from datetime import datetime

time = datetime.now().time().strftime("%I:%M:%S %p")
strtime = str(time)
print(strtime)
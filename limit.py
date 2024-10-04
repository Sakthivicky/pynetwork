import time
requestlist= []

def time_limit():
    timewindow=60
    maxlimit=5

    global requestlist

    currenttime=time.time()

    requestlist = [t for t in requestlist if currenttime - t < timewindow]

    if len(requestlist)< maxlimit:
     requestlist.append(currenttime)
     print(currenttime)

    else:
     waittime=timewindow-(currenttime-requestlist[0])
     print(f"please wait:{waittime}")

for i in range(10):
  time_limit()
  time.sleep(1)            
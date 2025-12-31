import time
from time import localtime
import ntptime
import gc

def main(argv):
  NTPSERVER="pool.ntp.org"
  try:
    ntptime.host=NTPSERVER
    ntptime.settime()
    print ("time sync'd with: " + NTPSERVER)
  except:
    print("Couldn't Sync time currently. Check Network connection.\n")

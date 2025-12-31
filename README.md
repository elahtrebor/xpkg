# xpkg
A micropython package manager for pushvm

A repo will be maintained in the packages directory.

the client xpkg.py must be installed on the Microcontroller device.

note if the package manager fails you can always just download the files in the package directory to your local computer and then use Thonny or Webrepl to push the files into the /lib directory of your microcontroller to use them with the shell.

To install and use:

create a /lib directory in the root of your microcontroller

copy xpkg.py into /lib<br>

Or download and run this installer file:  
[install_pushvm,py](https://github.com/elahtrebor/push/blob/main/pushvm/install_pushvm.py)

<pre>
Current list of packages:
testpkg    0.1.0 - test package for testing
wget       0.1.0 - Simple HTTP downloader
ping       0.1.0 - ICMP ping for MicroPython
ntpsync    0.1.0 - Sync Time with an NTP server
</pre>
<pre>
use the pushvm environment to execute the xpkg package manageer.
EXAMPLE:

>>> import pushvm
>>> pushvm.repl()
PUSH VM pushvm-complete-0.1
Type 'help'. Use 'exit' to quit.
Background: add '&' at end. Job control: jobs/kill/fg.
Interactive mode: live (background jobs run while you type)
push> xpkg list
ping      0.1.0 - ICMP ping for MicroPython
wget       0.1.0 - Simple HTTP downloader
testpkg    0.1.0 - test package for testing

push> xpkg install testpkg
connecting to: https://raw.githubusercontent.com/elahtrebor/xpkg/main
checking package list
defining source: https://raw.githubusercontent.com/elahtrebor/xpkg/main/packages/testpkg.py
defined destination: /lib/testpkg.py
installed testpkg

push> 
push> cd lib
lib
push> 
push> cat testpkg.py
import sys

def main(argv):
  return "ok"


push> testpkg
ok


push> 
push> xpkg install ping
connecting to: https://raw.githubusercontent.com/elahtrebor/xpkg/main
checking package list
defining source: https://raw.githubusercontent.com/elahtrebor/xpkg/main/packages/ping.py
defined destination: /lib/ping.py
installed ping

push> 
push> ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 64 data bytes
84 bytes from 8.8.8.8: icmp_seq=1, ttl=114, time=23.611000 ms
84 bytes from 8.8.8.8: icmp_seq=2, ttl=114, time=20.973000 ms
84 bytes from 8.8.8.8: icmp_seq=3, ttl=114, time=18.878000 ms
84 bytes from 8.8.8.8: icmp_seq=4, ttl=114, time=17.496000 ms
4 packets transmitted, 4 packets received
push> 
push> 
</pre>


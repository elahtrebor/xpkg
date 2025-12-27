# xpkg
A micropython package manager

A repo will be maintained in the packages directory.

the client xpkg.py must be installed on the Microcontroller device.

To install and use:

create a /lib directory in the root of your microcontroller

copy xpkg.py into /lib

use the pushvm shell to execute the xpkg package manageer.
EXAMPLE:

>>> import pushvm2
>>> pushvm2.repl()
PUSH VM pushvm-complete-0.1
Type 'help'. Use 'exit' to quit.
Background: add '&' at end. Job control: jobs/kill/fg.
Interactive mode: live (background jobs run while you type)
push> xpkg list
uping      0.1.0 - ICMP ping for MicroPython
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



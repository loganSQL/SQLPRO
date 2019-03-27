Get List of Users based on List of IPs
---------------------------------------

getListUserLogOnFromIP.ps1
--------------------------
Get the ip's from C:\logan\scripts\ip-addresses.txt
One by one, get the hostname from DNS, and query the explorer's user name from the host
Print IP,HOSTNAME,LogonUser
Write to C:\temp\ListOfUserLogOnFromIP.txt

get-userList.ps1
----------------
Usage:
	.\get-userList.ps1 -IPList yourIpListInputFilename -UserList yourUserListOutputFilename

get-user-from-IPList.ps1
------------------------
Usage:
	.\get-user-from-IPList.ps1 -IPList yourIpListInputFilename -UserList yourUserListOutputFilename

get-user-from-HostList.ps1
--------------------------
This script use PsLoggedon.exe 
Usage:
	.\get-user-from-HostList.ps1 -HostList yourHostListInputFilename -UserList yourUserListOutputFilename

Reference
----------
PsLoggedon.exe  
https://docs.microsoft.com/en-us/sysinternals/downloads/psloggedon
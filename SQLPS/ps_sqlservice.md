# Powershell Scripts for SQL Services
## [SQL Server Configuration Manager](<https://docs.microsoft.com/en-us/sql/relational-databases/sql-server-configuration-manager?view=sql-server-2017>)

* SQL Server 2017  C:\Windows\SysWOW64\SQLServerManager14.msc
* SQL Server 2016  C:\Windows\SysWOW64\SQLServerManager13.msc
* SQL Server 2014 (12.x)  C:\Windows\SysWOW64\SQLServerManager12.msc
* SQL Server 2012 (11.x)  C:\Windows\SysWOW64\SQLServerManager11.msc

## Start, Stop, Pause, Resume, Restart SQL Server Services

### Windows net commands: net start, net stop, net pause, net resume
```
###############
# SQL Service
###############
# To start the default instance of the Database Engine
net start "SQL Server (MSSQLSERVER)"
#-or-
net start MSSQLSERVER

# To start a named instance of the Database Engine
net start "SQL Server ( instancename )"
-or-
net start MSSQL$ instancename

# To start the Database Engine with startup options
Add startup options to the end of the net start "SQL Server (MSSQLSERVER)" statement, separated by a space. When started using net start, startup options use a slash (/) instead of a hyphen (-).

# -m single user mode
# -f starting sql instance with minima config
net start "SQL Server (MSSQLSERVER)" /f /m
-or-
net start MSSQLSERVER /f /m
#
# -m"SQLCMD"  => limits connections to a single connection and that connection must identify itself as the SQLCMD client program. Use this option when you are starting SQL Server in single-user mode and an unknown client application is taking the only available connection
#
# -m"Microsoft SQL Server Management Studio - Query"  => To connect through the Query Editor in Management Studio

###############
# SQL Agent
###############
net start "SQL Server Agent( instancename )"

-or-

net start SQLAgent$ instancename
```
### T-SQL
```
SHUTDOWN;
SHUTDOWN WITH NOWAIT;  
```
### Powershell (WMI)
```
# 1. which computer
###################
sqlps
# Get a reference to the ManagedComputer class.  
CD SQLSERVER:\SQL\computername  
$Wmi = (get-item .).ManagedComputer  
```
```
# 2. which service
##################
# To get a reference to the default instance of the Database Engine.
$DfltInstance = $Wmi.Services['MSSQLSERVER']  

# OR To get a reference to a named instance of the Database Engine.
# $DfltInstance = $Wmi.Services['MSSQL$instancename']  

# OR To get a reference to the SQL Server Agent service on the default instance of the Database Engine.
# $DfltInstance = $Wmi.Services['SQLSERVERAGENT']  

# OR To get a reference to the SQL Server Agent service on a named instance of the Database Engine.
# $DfltInstance = $Wmi.Services['SQLAGENT$instancename']  

# OR To get a reference to the SQL Server Browser service.
# $DfltInstance = $Wmi.Services['SQLBROWSER']  
```
```
# 3. what to do
################
# to start and then stop the selected service
# Display the state of the service.  
$DfltInstance  
# Start the service.  
$DfltInstance.Start();  
# Wait until the service has time to start.  
# Refresh the cache.  
$DfltInstance.Refresh();   
# Display the state of the service.  
$DfltInstance  
# Stop the service.  
$DfltInstance.Stop();  
# Wait until the service has time to stop.  
# Refresh the cache.  
$DfltInstance.Refresh();   
# Display the state of the service.  
$DfltInstance  
```

## Service Account Changes (SMO)
```
# Account and Password
$UName="MyDomain\MyServiceAccount"
$PWord="MySecretPwd"

# service : MSSQLSERVER
[System.Reflection.Assembly]::LoadWithPartialName("Microsoft.SqlServer.SqlWmiManagement") | out-null
$SMOWmiserver = New-Object ('Microsoft.SqlServer.Management.Smo.Wmi.ManagedComputer')
$SMOWmiserver.Services | select name, type, ServiceAccount, DisplayName, Properties, StartMode, StartupParameters | Format-List
$ChangeService=$SMOWmiserver.Services | where {$_.name -eq "MSSQLSERVER"}
$ChangeService
$ChangeService.SetServiceAccount($UName, $PWord)
$ChangeService | select name, type, ServiceAccount, DisplayName, Properties, StartMode, StartupParameters
Restart-Service -Force MSSQLSERVER
Get-Service "*SQL*"

# service : SQLSERVERAGENT
[System.Reflection.Assembly]::LoadWithPartialName("Microsoft.SqlServer.SqlWmiManagement") | out-null
$SMOWmiserver = New-Object ('Microsoft.SqlServer.Management.Smo.Wmi.ManagedComputer')
$SMOWmiserver.Services | select name, type, ServiceAccount, DisplayName, Properties, StartMode, StartupParameters | Format-List
$ChangeService=$SMOWmiserver.Services | where {$_.name -eq "SQLSERVERAGENT"}
$ChangeService
$ChangeService.SetServiceAccount($UName, $PWord)
$ChangeService | select name, type, ServiceAccount, DisplayName, Properties, StartMode, StartupParameters
Restart-Service -Force SQLSERVERAGENT
Get-Service "*SQL*"

```

## Change Startup Parameters
### To Single-user mode (SMO)
``` 
# To change to Single-User mode (SMO)
#######################################
[System.Reflection.Assembly]::LoadWithPartialName("Microsoft.SqlServer.SqlWmiManagement") | out-null
$SMOWmiserver = New-Object ('Microsoft.SqlServer.Management.Smo.Wmi.ManagedComputer')
$SMOWmiserver.Services | select name, type, ServiceAccount, DisplayName, Properties, StartMode, StartupParameters | Format-List
$ChangeService=$SMOWmiserver.Services | where {$_.name -eq "MSSQLSERVER"}
$ChangeService.StartupParameters
$oldparams=$ChangeService.StartupParameters
$oldparams
# The following to add -m to put SQL instance in single-user mode
$ChangeService.StartupParameters=$oldparams+";-m"
$ChangeService.StartupParameters
$ChangeService.Alter()
restart-service MSSQLSERVER
```
```
# to verify, sqlcmd and SSMS
sqlcmd -E
# to check errorlog
$env:COMPUTERNAME | Get-SqlErrorLog | Where-Object { $_.Text -match 'startup' }

# To change it back (Multi-user)
#################################
$ChangeService=$SMOWmiserver.Services | where {$_.name -eq "MSSQLSERVER"}
$ChangeService.StartupParameters
$oldparams
$ChangeService.StartupParameters = $oldparams
$ChangeService.StartupParameters
$ChangeService.Alter()
Restart-Service MSSQLSERVER
```
### [Set-DbaStartupParameter](<https://dbatools.io/functions/set-dbastartupparameter/>)

```
# To configure the SQL Instance server1\instance1 to startup up in Single User mode at next startup
Set-DbaStartupParameter -SqlServer server1\instance1 -SingleUser

# To append Trace Flags 8032 and 8048 to the startup parameters
Set-DbaStartupParameter -SqlServer server1\instance1 -SingleUser -TraceFlags 8032,8048

# To remove all trace flags and set SinguleUser to false
Set-DbaStartupParameter -SqlServer sql2016 -SingleUser:$false -TraceFlagsOverride
```

```
# backup the existing startup configuration
$StartupConfig = Get-DbaStartupParameter -SqlServer server1\instance1
# change the startup parameters ahead of some work
Set-DbaStartupParameter -SqlServer server1\instance1 -SingleUser -NoLoggingToWinEvents 
# then do stuff !!!
#fter the work has been completed, we can push the original startup parameters back
Set-DbaStartupParameter -SqlServer server1\instance1 -StartUpConfig $StartUpConfig
``

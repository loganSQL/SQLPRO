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

# -f starting sql instance with minima config and put it in single-user mode
net start "SQL Server (MSSQLSERVER)" /f /m
-or-
net start MSSQLSERVER /f /m

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
### Powershell
```
sqlps
# Get a reference to the ManagedComputer class.  
CD SQLSERVER:\SQL\computername  
$Wmi = (get-item .).ManagedComputer  

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
# to start and then stop the selected service as the following

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

## Service Account Changes
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
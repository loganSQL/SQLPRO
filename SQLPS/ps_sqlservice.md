# Powershell Scripts for SQL Services
## Service Account Changes
```
$UName="MyDomain\MyServiceAccount"
$PWord="MySecretPwd"

# MSSQLSERVER
[System.Reflection.Assembly]::LoadWithPartialName("Microsoft.SqlServer.SqlWmiManagement") | out-null
$SMOWmiserver = New-Object ('Microsoft.SqlServer.Management.Smo.Wmi.ManagedComputer')
$SMOWmiserver.Services | select name, type, ServiceAccount, DisplayName, Properties, StartMode, StartupParameters | Format-List
$ChangeService=$SMOWmiserver.Services | where {$_.name -eq "MSSQLSERVER"}
$ChangeService
$ChangeService.SetServiceAccount($UName, $PWord)
$ChangeService | select name, type, ServiceAccount, DisplayName, Properties, StartMode, StartupParameters
Restart-Service -Force MSSQLSERVER
Get-Service "*SQL*"

# SQLSERVERAGENT
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
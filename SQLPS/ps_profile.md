# Powershell Profile
## Location
```
# to display the current profile
$profile
# %UserProfile%\My Documents\WindowsPowerShell\profile.ps1 
C:\Users\logan.sql\Documents\WindowsPowerShell
```
## How to create it
```
# 1. Is the profile created?
test-path $profile

# 2. Create it
new-item -path $profile -itemtype file -force

# 3. Edit it
notepad $profile

# or
PowerShell_ISE –file $profile
```
## profile
```
$piper='C:\bin\piper.exe'
$opt='/q /l z /v C:\data\twitterfeed'
$vol=$piper+' '+$opt
$disopt=' /q /d z'
$disvol=$piper+' '+$disopt
$dd='get-psdrive –psprovider filesystem'
$vw='type z:\test.txt'
$qs='query session'
# need run as Admin
$gu='Get-Process -IncludeUserName|Select-Object -Unique -Property UserName'
# Alias
set-alias prun Invoke-Expression
set-alias lgsql Invoke-Sqlcmd
```
## Other Garbages
```
<# Powershell Env
# get
Get-Childitem env:
$env:computername
$Computer = $env:computername
$AppDataFolder = "$env:appdata"
$windows_path = $env:Path
$windows_path -split ';'
$powershell_path = $env:PSModulePath

# Set
$env:VariableName = 'new-value'
$env:path +=';c:\Batch'

# Delete
$env:VariableName = ''
#>

# remove the SET alias (normally used for set-variable)
if (test-path alias:set) { remove-item alias:set > $null }
function set
{
[string]$var = $args
if ($var -eq "")
{get-childitem env: | sort-object name}
else
{
if ($var -match "^(\S*?)\s*=\s*(.*)$")
{set-item -force -path "env:$($matches[1])" -value $matches[2];}
else
{write-error "ERROR Usage: VAR=VALUE"}
} 
}

<#
PowerShell Providers
In addition to environment variables, PowerShell providers also provide access to other data and components in a similar way - resembling a file system drive. This allows you to access many different types of data in a consistent way.
Built-in Providers
Alias - Windows PowerShell aliases {Alias}
Certificate - X509 certificates for digital signatures {cert}
Environment - Windows environment variables {Env}
FileSystem - File system drives, directories and files {filesystem} 
Function - Windows PowerShell functions {Function}
Registry - Windows registry {HKLM, HKCU}
Variable - Windows PowerShell variables {Variable}

Get-PsProvider
Get-psdrive

cd Alias:
ls or get-childitem

cd Function:
ls

cd HKCU:
ls

cd C:
ls

cd Variable:

#>

<#
# SQL Server PowerShell module

Install-Module -Name SqlServer

Get-Module SqlServer -ListAvailable

# limplicitly load the module 
Import-Module SqlServer
cd SQLSERVER:\SQL\MyHost\MyInstance
cd SQLSERVER:\SQL\localhost\DEFAULT
#>

Import-Module SqlServer

<#
cd SQLSERVER:\SQL\MySQLHost\DEFAULT\Databases
dir
cd msdb
invoke-sqlcmd "select db_name();"
invoke-sqlcmd -InputFile "C:\logan\scripts\test.sql"
lgsql "sp_help"
lgsql "sp_helpuser"
lgsql "sp_helpdb"
lgsql "sp_helplogins"
lgsql "sp_databases"
lgsql "sp_spaceused"

## 1. Looping sqlcmd
cd SQLSERVER:\SQL\MySQLHost\DEFAULT\Databases
$dbs=gci
#$dbs.name
foreach ($db in $dbs) {
  cd $db.name
  # also using script file $scriptfile="C:\temp\test.sql"
  # lgsql -InputFile $scriptfile
  lgsql "sp_databases"|format-table
  cd .. }
#

## Looping using $_
## For the variable for the current value in the pipe line.
## eg: 1,2,3 | %{ write-host $_ }  
cd SQLSERVER:\SQL\MySQLHost\DEFAULT\Databases
(gci .).name | %{ lgsql "sp_helpdb $_" }
#
(gci .).name | %{ lgsql "use $_; select db_name() as DB, name as TB from sysobjects where type='U'"
}
#>
<#
# Prompt for credentials to login into SQL Server
$serverInstance = "<your_server_instance>"
$credential = Get-Credential

# Load the SMO assembly and create a Server object
[System.Reflection.Assembly]::LoadWithPartialName('Microsoft.SqlServer.SMO') | out-null
$server = New-Object ('Microsoft.SqlServer.Management.Smo.Server') $serverInstance

# Set credentials
$server.ConnectionContext.LoginSecure=$false
$server.ConnectionContext.set_Login($credential.UserName)
$server.ConnectionContext.set_SecurePassword($credential.Password)

# Connect to the Server and get a few properties
$server.Information | Select-Object Edition, HostPlatform, HostDistribution | Format-List
# done
#>

<#
# Use Powershell to connect SQL on Linux
$srv = new-object Microsoft.SqlServer.Management.Smo.Server("MyHost")  
$conContext = $srv.ConnectionContext  
$conContext.LoginSecure = $FALSE  
$conContext.Login = "sa"  
$conContext.Password = "Xmas2017"  
$srv2 = new-object Microsoft.SqlServer.Management.Smo.Server($conContext)  
$srv2.Information | Select-Object Edition, HostPlatform, HostDistribution | Format-List
# Get ErrorLog
$srv2.ErrorLogPath
$srv2.ReadErrorLog(0)
# Get Databases
$srv2.Databases | where { $_.name -match 'logansql|master|model|msdb' }
$srv2.Databases | where { $_.name -match 'logansql' } | format-List
foreach ($db in $srv2.Databases) {
    $db.name,$db.size }
#>
<#
# Transferring Schema and Data from One Database to Another

#Connect to the local, default instance of SQL Server.  

#Get a server object which corresponds to the default instance  
#$srv2 = New-Object -TypeName Microsoft.SqlServer.Management.SMO.Server  

#Reference a database.  
$db = $srv2.Databases["logansql"]  

#Create a database to hold the copy of database  
$dbCopy = New-Object -TypeName Microsoft.SqlServer.Management.SMO.Database -argumentlist $srv2, "logansql_Copy"  
$dbCopy.Create()  

#Define a Transfer object and set the required options and properties.  
$xfr = New-Object -TypeName Microsoft.SqlServer.Management.SMO.Transfer -argumentlist $db  

#Set this objects properties  
$xfr.CopyAllTables = $true  
$xfr.Options.WithDependencies = $true  
$xfr.Options.ContinueScriptingOnError = $true  
$xfr.DestinationDatabase = "logansql_Copy"  
$xfr.DestinationServer = $srv2.Name  
$xfr.DestinationLoginSecure = $true  
$xfr.CopySchema = $true  
"Scripting Data Transfer"  
#Script the transfer. Alternatively perform immediate data transfer with TransferData method.  
$xfr.ScriptTransfer() 
#>

<#
Add-Type -AssemblyName ('Microsoft.SqlServer.Smo, Version=10.0.0.0, ' + `
                        'Culture=neutral, PublicKeyToken=89845dcd8080cc91')

$serverName = '.\SQLEXPRESS'
$smo = new-object Microsoft.SqlServer.Management.Smo.Server $serverName
$db  = $smo.Databases['AdventureWorks']
$tbl = $db.Tables | Where {$_.Schema -eq 'Production' -and `
                           $_.Name -eq 'Product'}

$output_file = "$home\foo.sql"

$scripter = new-object Microsoft.SqlServer.Management.Smo.Scripter $serverName
$scripter.Options.ScriptSchema = $false; 
$scripter.Options.ScriptData = $true; 
$scripter.Options.NoCommandTerminator = $true; 

if ($output_file -gt "")  
{ 
  $scripter.Options.FileName = $output_file 
  $scripter.Options.ToFileOnly = $true 
} 

# Output the script 
foreach ($s in $scripter.EnumScript($tbl)) { write-host $s } 
#>
```
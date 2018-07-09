# PowerShell Modules
## Installation
```
# When no scope is defined, or when the value of the Scope parameter is AllUsers, the module is installed to %systemdrive%:\Program Files\WindowsPowerShell\Modules
#
# 1. Find a module 
Find-Module -Name "SQL*"

# 2. Install a module by name
Install-Module -Name "ReportingServicesTools"

# 3. Install a specific version of a module
Install-Module -Name "ContosoServer" -RequiredVersion 1.1.3

# 4. Install the current version of a module
# When the value of Scope is CurrentUser, the module is installed to $home\Documents\WindowsPowerShell\Modules.
Install-Module -Name "ContosoServer" -Scope "CurrentUser"
```
## List & Import
### Get-InstalledModule
```
# gets Windows PowerShell modules that are installed on a computer.
Get-InstalledModule
```
### Get-Module
Windows PowerShell modules exist in two states: loaded (imported) and unloaded. Get-Module looks for available modules in the path specified by the $env:PSModulePath environment variable
```
# Get modules imported into the current session (only those imported)
Get-Module

# Get installed modules and available modules (where are they)
Get-Module -ListAvailable

# Get all exported files (it will list all the exported file locations)
Get-Module -ListAvailable -All

# Get a module detail
Get-Module -name "sqlserver" |Format-List

# Display the contents of a module manifest in a specific path
$m = Get-Module -list -Name SqlServer
Get-Content $m.Path
```
Get-Module gets modules, but it does not import them. Starting in Windows PowerShell 3.0, modules are automatically imported when you use a command in the module, but a Get-Module command does not trigger an automatic import. You can also import the modules into your session by using the *Import-Module* cmdlet.

Starting in Windows PowerShell 3.0, you can get and then, import modules from remote sessions into the local session. This strategy uses the Implicit Remoting feature of Windows PowerShell and is equivalent to using the *Import-PSSession* cmdlet. When you use commands in modules imported from another session, the commands run implicitly in the remote session. This feature lets you manage the remote computer from the local session.
```
# USING PSSession
#################
# Get modules installed on a remote computer
# 1. create a PSSession on the Server01 computer, saves it in the $s variable.
$s = New-PSSession -ComputerName Server01
# 2. get the modules in the PSSession in the $s variable
Get-Module -PSSession $s -ListAvailable

# Run Powershell on Remote Machine
# Enable-PSRemoting -Force
# Disable-PSRemoting -Force
##################################
# 0. Check whether the remote MyServer opened (Admin)
New-PSSession -ComputerName MyServer
Get-PSSessionConfiguration | Format-Table -Property Name, Permission -Auto
# 1. Enter PSSession
# Enter-PSSession -ComputerName COMPUTER -Credential USER
Enter-PSSession -ComputerName MyRemoteMachine
$env:COMPUTERNAME
Get-Module -ListAvailable
Import-Module SqlServer
# Or
# 2. Execute a Single Remote Command
# Invoke-Command -ComputerName COMPUTER -ScriptBlock { COMMAND } -credential USERNAME
Invoke-Command -ComputerName MyServer -ScriptBlock { $ENV:COMPUTERNAME }


```
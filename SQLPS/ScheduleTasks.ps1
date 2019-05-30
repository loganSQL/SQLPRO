<#
Audit the tasks
#>
# Get all the tasks
$Tasks = Get-ScheduledTask
$Tasks

# Find a specific task
$Tasks|where-object taskname -Match "CheckIn"

$MyTask = $Tasks|where-object taskname -Match "CheckIn"| Select-Object -Property *
$MyTask.Triggers
$MyTask.Triggers.Repetition

$MyTask.Actions
$MyTask.Actions.Arguments

$MyTask.Principal

# Find all tasks owned by UserID
Get-ScheduledTask |Where {$_.Principal.UserID  -eq 'logan.chen'}

<#
Create a new task
#>
Import-Module TaskScheduler 
$task = New-Task
$task.Settings.Hidden = $true
Add-TaskAction -Task $task -Path C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe –Arguments “-File C:\logan\scripts\testjob1.ps1”
Add-TaskTrigger -Task $task -Daily -At “10:00”
Register-ScheduledJob –Name ”My Test Job1” -Task $task

<#
Other trigger options that could be useful in creating new tasks include:
-AtStartup — Triggers your task at Windows startup.
-AtLogon — Triggers your task when the user signs in.
-Once — Triggers your task once. You can set a repetition interval using the –RepetitionInterval parameter.
-Weekly — Triggers your task once a week.
#>
$Trigger= New-ScheduledTaskTrigger -At 10:00am –Daily # Specify the trigger settings
$User= "NT AUTHORITY\SYSTEM" # Specify the account to run the script
$Action= New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "C:\logan\scripts\testjob2.ps1" # Specify what program to run and with its parameters
Register-ScheduledTask -TaskName "My Test Job2" -Trigger $Trigger -User $User -Action $Action -RunLevel Highest –Force # Specify the name of the task

<#
#>
Import-Module ScheduledTasks 
$action = New-ScheduledTaskAction -Execute 'Powershell.exe' -Argument '-NoProfile -WindowStyle Hidden -command "& {get-eventlog -logname Application -After ((get-date).AddDays(-1)) | Export-Csv -Path c:\temp\applog.csv -Force -NoTypeInformation}"' 
$trigger =  New-ScheduledTaskTrigger -Daily -At 9am 
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "AppLog" -Description "Daily dump of Applog"

<#
Export a scheduled task
#>
Export-ScheduledTask "Weekly System Info Report"
#
Export-ScheduledTask "Weekly System Info Report" | out-file \\myhost\e$\MyTask.xml
#
Get-ScheduledTask | foreach {
 
    Export-ScheduledTask -TaskName $_.TaskName -TaskPath $_.TaskPath |
     
    Out-File (Join-Path "\\myhost\e$" "$($_.TaskName).xml") -WhatIf
}
#
get-scheduledtask -TaskName "*Windowsbackup" -CimSession MYRemoteHost  | Export-ScheduledTask | out-file \\myhost\e$\WindowsBackup.

<#
Import a scheduled task
#>
Register-ScheduledTask -Xml '\\myhost\e$\MyTask.xml' -TaskName "Weekly System Info Report"
#
Register-ScheduledTask -Xml (get-content '\myhost\e$\MyTask.xml' | out-string) -TaskName "Weekly System Info Report"
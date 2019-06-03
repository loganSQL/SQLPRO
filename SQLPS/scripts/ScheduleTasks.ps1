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
Get-ScheduledTask |Where {$_.Principal.UserID  -eq 'logansql'}


<#
Export a scheduled task
#>
Export-ScheduledTask "CheckIn"
Export-ScheduledTask "CheckIn" | out-file C:\temp\CheckIn.xml

<# Here is output file as XML format
<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Date>2019-05-24T14:49:40.1107366</Date>
    <Author>MYDomain\logansql</Author>
    <URI>\CheckIn</URI>
  </RegistrationInfo>
  <Principals>
    <Principal id="Author">
      <UserId>S-1-5-21-647314393-1024732314-934288641-31517</UserId>
      <LogonType>InteractiveToken</LogonType>
      <RunLevel>HighestAvailable</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <RunOnlyIfNetworkAvailable>true</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
  </Settings>
  <Triggers>
    <TimeTrigger>
      <StartBoundary>2019-05-24T08:05:00</StartBoundary>
      <Repetition>
        <Interval>PT10M</Interval>
        <Duration>P1D</Duration>
      </Repetition>
    </TimeTrigger>
  </Triggers>
  <Actions Context="Author">
    <Exec>
      <Command>powershell</Command>
      <Arguments>C:\logan\scripts\CheckIn.ps1</Arguments>
    </Exec>
  </Actions>
</Task>
#>

$mytask = Get-ScheduledTask |Where taskname -eq 'CheckIn'
$MyTask
$MyTask|Stop-ScheduledTask
$mytask = Get-ScheduledTask |Where taskname -eq 'CheckIn'
# Need Run As Admin , to Unregister the Task
$MyTask|Unregister-ScheduledTask

# Need Run As Admin , to Unregister the Task
Register-ScheduledTask -Xml 'C:\temp\CheckIn.xml' -TaskName "CheckIn"
# if the above complaint: Register-ScheduledTask : The task XML is malformed.
# Try the following
Register-ScheduledTask -Xml (get-content 'C:\temp\CheckIn.xml' | out-string) -TaskName "CheckIn"


<#
export all the tasks
#>
#
Get-ScheduledTask | foreach {
 
    Export-ScheduledTask -TaskName $_.TaskName -TaskPath $_.TaskPath |
     
    Out-File (Join-Path "\\myhost\e$" "$($_.TaskName).xml") -WhatIf
}
# export a task from remotehost
get-scheduledtask -TaskName "*Windowsbackup" -CimSession MYRemoteHost  | Export-ScheduledTask | out-file \\myhost\e$\WindowsBackup.

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
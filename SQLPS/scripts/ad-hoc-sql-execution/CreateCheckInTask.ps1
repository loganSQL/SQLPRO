<#
# Export a scheduled task

Export-ScheduledTask "CheckIn"
Export-ScheduledTask "CheckIn" | out-file C:\temp\CheckIn.xml

#>

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

<#
$mytask = Get-ScheduledTask |Where taskname -eq 'CheckIn'
$MyTask
$MyTask|Stop-ScheduledTask
$mytask = Get-ScheduledTask |Where taskname -eq 'CheckIn'
# Need Run As Admin , to Unregister the Task
$MyTask|Unregister-ScheduledTask
#>


# Need Run As Admin , to Unregister the Task
Register-ScheduledTask -Xml 'C:\temp\CheckIn.xml' -TaskName "CheckIn"
# if the above complaint: Register-ScheduledTask : The task XML is malformed.
# Try the following
Register-ScheduledTask -Xml (get-content 'C:\temp\CheckIn.xml' | out-string) -TaskName "CheckIn"
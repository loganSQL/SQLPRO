# Powershell Outlook Mail
## Basic 
```
#
# Simple Email
# start outlook on the host first
$Outlook = New-Object -ComObject Outlook.Application
$Mail = $Outlook.CreateItem(0)
$Mail.To = "logan.sql@outlook.com"
$Mail.Subject = "Hello"
$Mail.Body ="Lucky day!"
$Mail.Send()
```
## Attach File
```
$Outlook = New-Object -ComObject Outlook.Application
$Mail = $Outlook.CreateItem(0)
$Mail.To = "logan.sql@outlook.com"
$Mail.Subject = "SQL script"
$Mail.Body ="Please see the script attached"
#$Mail.HTMLBody = "Please see the script attached"
$File = "C:\temp\test.sql"
$Mail.Attachments.Add($File)
$Mail.Send()
```

## More
```
Process {
# Create an instance Microsoft Outlook
$Outlook = New-Object -ComObject Outlook.Application
$Mail = $Outlook.CreateItem(0)
$Mail.To = "logan.sql@outlook.com"
$Mail.Subject = "SQL script"
$Mail.Body ="Please see the script attached"
#$Mail.HTMLBody = "Please see the script attached"
$File = "C:\temp\test.sql"
$Mail.Send()
       } # End of Process section
End {
# Section to prevent error message in Outlook
$Outlook.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($Outlook)
$Outlook = $null
   } # End of End section!
```

## Check outlook process running or not
```
# because of security, the following must run under the user account, and not run ps as ADMIN
#
# 1.  Outlook Object
#     Check outlook process running or not
#     if yes, get the object, if not, start outlook and get the object
$YourEmailAddress='logan.sql@outlook.com'
$ProcessName = "outlook"
If ($Process = (Get-Process -Name $ProcessName -ErrorAction SilentlyContinue)) {
  "$($ProcessName) is running. Just get it." | Write-Host
  $outlook = [Runtime.Interopservices.Marshal]::GetActiveObject('Outlook.Application')
} else {
  "$($ProcessName) is NOT running. Starting it." | Write-Host
  Start-Process Outlook
  $outlook = New-Object -com Outlook.Application
}
$namespace = $Outlook.GetNameSpace("MAPI")
#
# 2.  specify the originating folder (the Inbox)
#     specify the folder to copy to (SQLAlerts)
#     create a new rule ("My rule1: Receiving SQLAlerts")
#
$inbox = $namespace.GetDefaultFolder([Microsoft.Office.Interop.Outlook.OlDefaultFolders]::olFolderInbox)
$MyFolder1 = $namespace.Folders.Item($YourEmailAddress).Folders.Item('SQLAlerts')
$rules = $namespace.DefaultStore.GetRules()
$rule = $rules.create("My rule1: Receiving SQLAlerts", [Microsoft.Office.Interop.Outlook.OlRuleType]::olRuleReceive)
#
# 3.  Try to poke around the folds
#
# Top folder
$namespace.Folders
$namespace.Folders |select Name, FolderPath
# Private folder
$namespace.Folders.Item(1)|select Name, FolderPath
# Public folder
$namespace.Folders.Item(2)|select Name, FolderPath
# all the folder under Private folder
$namespace.Folders.Item(1).Folders|select Name, FolderPath
# all the folder uder Public folder
$namespace.Folders.Item(2).Folders|select Name, FolderPath
# SQLAlerts folder is here
$namespace.Folders.Item(1).Folders.Item("SQLAlerts")
$namespace.Folders.Item(1).Folders.Item("SQLAlerts")|select Name, FolderPath
# show the folders under it, if any
$namespace.Folders.Item(1).Folders.Item("SQLAlerts").Folders
# show the items (emails) in it
$namespace.Folders.Item(1).Folders.Item("SQLAlerts").Items
$namespace.Folders.Item(1).Folders.Item("SQLAlerts").Items | select To, Subject, SenderName, Body | format-list
#
# 4.  First Rule
#
<#
The first line relates the rule to the subject line of an incoming e-mail. The string to look for (“Completed Notification”) is specified, and the action to take is CopyToFolder (as opposed, for example, MoveToFolder). The invocation recites the action and the destination folder.
#>
$rule_body = $rule.Conditions.Subject
$rule_body.Enabled = $true
$rule_body.Text = @('SQL Server Message')
$action = $rule.Actions.MoveToFolder
$action.enabled = $true
[Microsoft.Office.Interop.Outlook._MoveOrCopyRuleAction].InvokeMember("Folder", [System.Reflection.BindingFlags]::SetProperty, $null, $action, $MyFolder1)
$rules.Save()
```

## get the outlook process
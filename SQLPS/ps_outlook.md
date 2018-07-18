# Powershell Outlook Mail
## Get Outlook Object
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
```
#
# Simple Send Email
# 
```
# Get Outlook Object Above
# $Outlook = New-Object -ComObject Outlook.Application
$Mail = $Outlook.CreateItem(0)
$Mail.To = "logan.sql@outlook.com"
$Mail.Subject = "Hello"
$Mail.Body ="Lucky day!"
$Mail.Send()
```
## Attach File
```
# Get Outlook Object Above
# $Outlook = New-Object -ComObject Outlook.Application
$Mail = $Outlook.CreateItem(0)
$Mail.To = "logan.sql@outlook.com"
$Mail.Subject = "SQL script"
$Mail.Body ="Please see the script attached"
#$Mail.HTMLBody = "Please see the script attached"
$File = "C:\temp\test.sql"
$Mail.Attachments.Add($File)
$Mail.Send()
```

## Process and Error Handling
```
Process {
# Get Outlook Object Above
# $Outlook = New-Object -ComObject Outlook.Application
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

## Folders & Rules
[PowerShell - Managing an Outlook Mailbox with PowerShell](<https://msdn.microsoft.com/en-us/magazine/dn189202.aspx>)
```
# because of security, the following must run under the user account, and not run ps as ADMIN
#
# 1.  Outlook Object
# Get Outlook Object Above
# $Outlook = New-Object -ComObject Outlook.Application
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
# 3.  Try to poke around the folders
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

## [By Example – PowerShell commands for Outlook](<https://sqlnotesfromtheunderground.wordpress.com/2014/09/06/by-example-powershell-commands-for-outlook/>)
```
#########################################################################################
## Outlook Commands by Example
#########################################################################################
 
 
#########################################################################################
## Connect to Outlook
 
# Outlook Connection
$Outlook = New-Object -ComObject Outlook.Application
 
## Listing Folders in Outlook (Shows Email, Calendar, Tasks etc)
$OutlookFolders = $Outlook.Session.Folders.Item(1).Folders
$OutlookFolders | ft FolderPath
 
## Using Default 
$OutlookDeletedITems = $Outlook.session.GetDefaultFolder(3)
$outlookOutbox = $Outlook.session.GetDefaultFolder(4)
$OutlookSentItems = $Outlook.session.GetDefaultFolder(5)
$OutlookInbox = $Outlook.session.GetDefaultFolder(6)
$OutlookCalendar = $Outlook.session.GetDefaultFolder(9)
$OutlookContacts = $Outlook.session.GetDefaultFolder(10)
$OutlookJournal = $Outlook.session.GetDefaultFolder(11)
$OutlookNotes = $Outlook.session.GetDefaultFolder(12)
$OutlookTasks = $Outlook.session.GetDefaultFolder(13)
 
 
#########################################################################################
## Inbox Folders
 
# List all Folders 
$Outlook.Session.Folders.Item(1).Folders.Item(&quot;Inbox&quot;).Folders | ft FullFolderPath 
 
# Create folder
$Outlook.Session.Folders.Item(1).Folders.Item(&quot;Inbox&quot;).Folders.Add(&quot;Scripts Received&quot;)
 
# Delete Folder
$OutlookFolderToDelete = $Outlook.Session.Folders.Item(1).Folders.Item(&quot;Inbox&quot;).Folders.Item(&quot;Scripts Received&quot;)
$OutlookFolderToDelete.Delete()
 
 
#########################################################################################
## Inbox Email
 
## Navigating to Sub folder of Inbox called Daily Tasks
$Outlook.Session.Folders.Item(1).Folders.Item(&quot;Inbox&quot;).Folders.Item(&quot;Daily Tasks&quot;)
 
# Read All Emails in a Folder Path Inbox -&amp;gt; SPAM Mail
$EmailsInFolder = $Outlook.Session.Folders.Item(1).Folders.Item(&quot;Inbox&quot;).Folders.Item(&quot;SPAM Folder&quot;).Items
$EmailsInFolder | ft SentOn, Subject, SenderName, To, Sensitivity -AutoSize -Wrap
 
# Send an Email from Outlook
$Mail = $Outlook.CreateItem(0)
$Mail.To = &quot;stephen@badseeds.local&quot;
$Mail.Subject = &quot;Action&quot;
$Mail.Body =&quot;Pay rise please&quot;
$Mail.Send()           
 
# Delete an Email from the folder Inbox with Subject Title &quot;Action&quot;
$EmailInFolderToDelete = $Outlook.Session.Folders.Item(1).Folders.Item(&quot;Inbox&quot;).Items
$EmailInFolderToDelete | ft SentOn, Subject, SenderName, To, Sensitivity -AutoSize -Wrap
$EmailToDelete = $EmailInFolderToDelete | Where-Object {$_.Subject -eq &quot;Action&quot;}
$EmailToDelete.Delete()
 
# Delete All Emails in Folder.Items
$EmailsInFolderToDelete = $Outlook.Session.Folders.Item(1).Folders.Item(&quot;Inbox&quot;).Folders.Item(&quot;SPAM Folder&quot;).Items
foreach ($email in $EmailsInFolderToDelete)
    {
        $email.Delete()
    }
 
# Move Emails from Inbox to Test folder
$EmailIToMove = $Outlook.Session.Folders.Item(1).Folders.Item(&quot;Inbox&quot;).Items
$EmailIToMove | ft SentOn, Subject, SenderName, To, Sensitivity -AutoSize -Wrap
$NewFolder = $Outlook.Session.Folders.Item(1).Folders.Item(&quot;Inbox&quot;).Folders.Item(&quot;test&quot;)
 
FOREACH($Email in $EmailIToMove )
    { 
        $Email.Move($NewFolder) 
    }
 
  
#########################################################################################
## Calender
 
## Connect to Calendar 
$OutlookCalendar = $Outlook.session.GetDefaultFolder(9)
 
# Read Calendar 
$OutlookCalendar.Items | ft subject, start
 
# Create New Calendar Item
$NewEvent = $Outlook.CreateItem(1)
$NewEvent.Subject = &quot;Timmys Birthday&quot;
$NewEvent.Start = [datetime]”10/9/2014&quot;
$NewEvent.save()
 
# Create re-occuring Event
$NewEvent = $Outlook.CreateItem(1)
$NewEvent.Subject = &quot;Timmys Birthday&quot;
$NewEvent.Start = [datetime]”10/9/2014&quot;
$Recur = $NewEvent.GetRecurrencePattern()
$Recur.Duration=1440
$Recur.Interval=12
$Recur.RecurrenceType=5
$Recur.Noenddate=$TRUE
$NewEvent.save()
 
# Delete Event - Timmys Birthday
$TimmyCalendar = $OutlookCalendar.Items | WHERE {$_.Subject -eq &quot;Timmys Birthday&quot;}
$TimmyCalendar.Delete()
 
 
#########################################################################################
## Tasks
 
# Read Tasks
$OutlookTasks = $Outlook.session.GetDefaultFolder(13).Items
$OutlookTasks | ft Subject, Body
 
# Create a task
$newTaskObject =  $Outlook.CreateItem(&quot;olTaskItem&quot;)
$newTaskObject.Subject = &quot;New Task&quot;
$newTaskObject.Body = &quot;This is the main text&quot;
$newTaskObject.Save()
 
# Delete a task
$OutlookTasks = $Outlook.session.GetDefaultFolder(13).Items
$DeleteTask = $OutlookTasks | Where-Object {$_.Subject -eq &quot;New Task&quot;}
$DeleteTask.Delete()
 
# Edit a task
$OutlookTasks = $Outlook.session.GetDefaultFolder(13).Items
$Task = $OutlookTasks | Where-Object {$_.Subject -eq &quot;New Task&quot;}
$Task.Body = &quot;Updated Results&quot;
$Task.Save()
 
 
#########################################################################################
## Contacts
 
# Read Contacts
$OutlookContacts = $Outlook.session.GetDefaultFolder(10).items
$OutlookContacts| Format-Table FullName,MobileTelephoneNumber,Email1Address
 
# Add a Contact
$OutlookContacts = $Outlook.session.GetDefaultFolder(10)
$NewContact = $OutlookContacts.Items.Add()
$NewContact | gm
$NewContact.FullName = &quot;John&quot;
$NewContact.Email1Address = &quot;John@Badseeds.local&quot;
$NewContact.Save()
 
# Delete Contact Full Name - &quot;John&quot;
$OutlookContacts = $Outlook.session.GetDefaultFolder(10).items
$DeleteJohn = $OutlookContacts | Where-Object {$_.FullName -eq &quot;John&quot;}
$DeleteJohn.Delete()
 
# Update Contact
$OutlookContacts = $Outlook.session.GetDefaultFolder(10).items
$John = $OutlookContacts | Where-Object {$_.FullName -eq &quot;John&quot;}
$John.CompanyName = &quot;BadSeeds&quot;
$John.Save()
```
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
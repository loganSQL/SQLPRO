[CmdletBinding()]

# .\SQLStep.ps1 -servername SERVERNAME -dbname DBNAME -requestpath REQUESTPATH -scriptprefix scriptprefix 
# Example
# .\SQLStep.ps1 -servername MySQL -dbname MyDB -requestpath 'F:\MyRequest' -scriptprefix Ad-Hoc-Script
Param (
  [string]$servername,
  [string]$dbname,
  [string]$requestpath,
  [string]$scriptprefix
)

if (!$servername -or !$dbname -or !$requestpath -or !$scriptprefix )
{
'.\SQLStep.ps1 -servername SERVERNAME -dbname DBNAME -requestpath REQUESTPATH -scriptprefix scriptprefix'	
 exit
}

$date = (Get-Date).ToString("yyyy-MM-dd")
$time = (Get-Date).ToString("yyyyMMdd_hhmm")

$ScriptDir = $requestpath + '\Daily'
$scriptDir
Set-Location $ScriptDir


$scriptprefix=$scriptprefix+'*'
$Step=Get-Item $scriptprefix
if (!$Step)
{
 Write-output 'No file exists'
 exit
}

$OutputDir = $requestpath + '\History\'+$date
if(!(Test-Path -Path $OutputDir )){
    New-Item -ItemType directory -Path $OutputDir
}

Get-Item $scriptprefix | 
Foreach-Object {

$StepFullName=$_.FullName
$StepName=$_.Name
$StepBaseName=$_.BaseName
$InputScript=$StepFullName
$OutputText=$OutputDir+'\'+$time+'_'+$StepBaseName+'.txt'

$InputScript
$StepFullName
$OutputText

# execute the script
sqlcmd -E -S $servername -d $dbname -i $StepFullName -e -o $OutputText

# move the script to history (maybe the same script run many times)
$CopyNewName=$OutputDir+'\'+$time+'_'+$StepBaseName+'.sql'
Copy-Item -Path $StepFullName -Destination $CopyNewName
Remove-Item $StepFullName

#Move-Item -Path $StepFullName -Destination $OutputDir
$maillist = 'MyTeam@outlook.com;logansql@outlook.com'
$mailsubject = 'MyQL '+$scriptprefix

# send email
$sendmailsql="exec msdb..sendOutputEmail '{0}','{1}','{2}'" -f $mailsubject,$OutputText,$maillist
sqlcmd -E -S $servername -d $dbname -Q $sendmailsql
}

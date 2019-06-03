$servername = 'MYSQL'
$dbname = 'tempdb'
$source = "C:\MyRequest"
$destination = "\\"+$servername+"\E$\myrequest\Daily"


if (!(Test-Path -Path "$source\*"))
{
    # empty
    '{0} is empty' -f $source
    exit 0
}

if (Test-Path -Path "$destination\*")
{
    # Not empty
    '{0} is not empty' -f $destination
    #exit 0
}


mv $source\*.sql $destination
del $source\*


$checkInLog="\\"+$servername+"\f$\fnrequest\CheckInLog\"
#$date = (Get-Date).ToString("yyyy-MM-dd")
$time = (Get-Date).ToString("yyyyMMdd_hhmm")
$CheckInLogText=$checkInLog+'\'+$time+'.txt'
$date+' Scripts have been checked in to the following directory'>$CheckInLogText
dir $destination >> $CheckInLogText
"" >> $CheckInLogText
"The above script will be scheduled for the next execution." >> $CheckInLogText
"" >> $CheckInLogText
"You will be notified by an email with the output result.">> $CheckInLogText

$OutputText="f:\myrequest\CheckInLog\"+$time+'.txt'

$maillist = 'MyTeam@outlook.com;logansql@outlook.com'
#$maillist = 'logan.chen@firstnational.ca'
# send email
$sendmailsql="exec msdb..sendOutputEmail '{0}','{1}','{2}'" -f 'MYSQL CheckIn/Schedule Process',$OutputText, $maillist
sqlcmd -E -S $servername -d $dbname -Q $sendmailsql
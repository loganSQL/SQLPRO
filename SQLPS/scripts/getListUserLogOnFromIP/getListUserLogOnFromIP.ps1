<#
$ipAddress="196.18.50.151"
$hostName=[System.Net.Dns]::GetHostByAddress($ipAddress).Hostname
(Get-WmiObject -Class win32_process -ComputerName $hostName | Where-Object name -Match explorer).getowner().user
#>

$MyOutput = "C:\temp\ListOfUserLogOnFromIP.txt"
"IPAddress : HostName : UserLoggedOnLocally">$MyOutput
"---------   --------   -------------------">>$MyOutput
Get-Content C:\logan\scripts\ip-addresses.txt | ForEach-Object{
    $hostname = ([System.Net.Dns]::GetHostByAddress($_)).Hostname
    if($? -eq $False) {
      $hostname ="Cannot resolve hostname"
      }
    else
      {
      $username = (Get-WmiObject -Class win32_process -ComputerName $hostname | Where-Object name -Match explorer).getowner().user
      if($? -eq $False) {
        $username ="No one is logged on locally"
        }
      }
    $_ +" : "+ $hostname +" : "+ $username >> $MyOutput
}
get-content $MyOutput
[CmdletBinding()]
Param (
  [string]$IPList,
  [string]$UserList
)

#

<#
$ipAddress="196.18.50.151"
$hostName=[System.Net.Dns]::GetHostByAddress($ipAddress).Hostname
(Get-WmiObject -Class win32_process -ComputerName $hostName | Where-Object name -Match explorer).getowner().user
#>

if (!$IPList -or !$UserList )
{
'get current logged on UserList from IPList'
'.\get-userList.ps1 -IPList yourIpListInputFilename -UserList yourUserListOutputFilename'	
 exit
}
else
{
'get-userList.ps1 {0}, {1}' -f $IPList, $UserList
}

$MyInput = $IPList
$MyOutput = $UserList
"IPAddress : HostName : UserLoggedOnLocally">$MyOutput
"---------   --------   -------------------">>$MyOutput
Get-Content $MyInput | ForEach-Object{
    $hostname = ([System.Net.Dns]::GetHostByAddress($_)).Hostname
    if($? -eq $False) {
      $hostname ="Cannot resolve hostname"
      }
    else
      {
      $has_explorer = Get-WmiObject -Class win32_process -ComputerName $hostname | Where-Object name -Match explorer
      if ($has_explorer) {
        $username = $has_explorer.getowner().user
        }
      else
        {
        $username ="No one is logged on locally"
        }
      }
    $_ +" : "+ $hostname +" : "+ $username >> $MyOutput
}
get-content $MyOutput
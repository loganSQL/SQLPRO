
$group = "Administrators"
$members= Get-LocalGroupMember -Group $group
$admins=get-content "C:\logan\scripts\validuserlist.txt"
foreach ($member in $members.name)
{
	if ($admins.Contains($member))
		{$member}
	else
		{
		write-output "remove..."
 		$member
		Remove-LocalGroupMember -Group $group -Member $member –Verbose
 		}
}
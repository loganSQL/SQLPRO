cleanAdminGroup.ps1
-------------------
The powershell script to check the list of users in 'validuserlist.txt', and compare with the existing users in the local group 'Administrators'. Remove them if not in the validuserlist.

runasadmin.bat
--------------
The batch script to start the above powershell script as aministrator. It can be called by task scheduler to automate the task.


Reference
---------
Use a batch file to run your PowerShell scripts
https://code.adonline.id.au/use-a-batch-file-to-run-your-powershell-scripts/
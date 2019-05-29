# Git For Windows
## Git Server
[Setting up a Git server on Windows using Git for Windows and Win32_OpenSSH](<https://github.com/PowerShell/Win32-OpenSSH/wiki/Setting-up-a-Git-server-on-Windows-using-Git-for-Windows-and-Win32_OpenSSH>)
### Install Win32 OpenSSH
[Install Win32 OpenSSH (test release)](<https://github.com/PowerShell/Win32-OpenSSH/wiki/Install-Win32-OpenSSH>)
* [How to retrieve links to latest packages](<https://github.com/PowerShell/Win32-OpenSSH/wiki/How-to-retrieve-links-to-latest-packages>)

To get the latest download link:
```
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$url = 'https://github.com/PowerShell/Win32-OpenSSH/releases/latest/'
$request = [System.Net.WebRequest]::Create($url)
$request.AllowAutoRedirect=$false
$response=$request.GetResponse()
$([String]$response.GetResponseHeader("Location")).Replace('tag','download') + '/OpenSSH-Win64.zip'  
$([String]$response.GetResponseHeader("Location")).Replace('tag','download') + '/OpenSSH-Win32.zip'
```
* [MyDownload of OpenSSH](<https://github.com/PowerShell/Win32-OpenSSH/releases/tag/v7.9.0.0p1-Beta>)
Download OpenSSH-Win64.zip

* Extract contents of the latest build to C:\Program Files\OpenSSH
* In an elevated Powershell console, run the following
```
cd '\Program Files\OpenSSH'
powershell.exe -ExecutionPolicy Bypass -File install-sshd.ps1
```

* Open the firewall for sshd.exe to allow inbound SSH connections
```
netsh advfirewall firewall add rule name=sshd dir=in action=allow protocol=TCP localport=22
```

* Start sshd

This will automatically generate host keys under %programdata%\ssh if they don't already exist
```
net start sshd
```

* Setup sshd service to auto-start
```
Set-Service sshd -StartupType Automatic
```
### Unintall Win32 OpenSSH
```
cd 'C:\Program Files\OpenSSH
powershell.exe -ExecutionPolicy Bypass -File uninstall-sshd.ps1
```
## Install Git for Windows
### download [Git-2.21.0-64-bit](<https://gitforwindows.org/>)
### Installation
* C:\Program Files\Git
* Components (Git Bash, Git GUI, associate .git*, .sh)
* Git Terminal (MINGW64)
### Setup and Configuration
* Set system environment variable for sshd to pick up the git commands
```
$gitPath = Join-Path -Path $env:ProgramFiles -ChildPath "git\mingw64\bin"
$machinePath = [Environment]::GetEnvironmentVariable('Path', 'MACHINE')
[Environment]::SetEnvironmentVariable('Path', "$gitPath;$machinePath", 'Machine')
```
* Restart sshd service so the PATH environment can take effect
```
get-service sshd
stop-service sshd
start-service sshd
get-service sshd
```
* [First-Time Git Setup](<https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup>)
```
git config --list --show-origin

git config --global user.name "John Doe"
git config --global user.email johndoe@example.com

git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -nosession"

git config --global core.editor "'C:/Program Files (x86)/Notepad++/notepad++.exe' -multiInst -nosession"

git config --list

git config --show-origin rerere.autoUpdate
```
### [Create A Git Server](<https://medium.com/@piteryo7/how-to-set-up-git-server-on-local-network-windows-tutorial-7ec5cd2df3b1>)
* Go to folder ( like D:\GitServer)
* RightCLike Open Git Bash
* Create a central Git repository on Git Server
```
git init LoganSQLGitRepos.git --bare
```
```
Initialized empty Git repository in D:/GitServer/LoganSQLGitRepos.git/
```
* Choose where you want to initialize client repository and open git bash there and local host.
```
git clone <path_to_your_server>
```
* [Generating a new SSH key](<https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent>)
```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
### Connect From the Remote Client (Git Bash)
```
## check the SSH file
ls -latr *.pub
cd .ssh/
ls -latr

## since the SSH key there, you should be able to clone it remotely
cd /c/temp
git clone //YourGitServerHost/GitServer/LoganSQLGitRepos.git/
```
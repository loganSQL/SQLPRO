# MSSQL-Scripter
## 1. [microsoft/mssqlscripter](<https://github.com/Microsoft/mssql-scripter>)
```
## Check Python
C:\> python

## 
C:\> pip install mssql-scripter 
```
[More detail for both Windows and Linux](<https://www.sqlshack.com/all-about-mssql-scripter-the-sql-server-cross-platform-scripting-tool/>)
## 2. [Examples](<https://www.mssqltips.com/sqlservertip/5913/mssqlscripter-tool-and-examples-to-generate-scripts-for-sql-server-objects/>)
```
## help
mssql-scripter -h
```
```
PS C:\logan\Python3> mssql-scripter -h
usage: mssql-scripter [-h] [--connection-string  | -S ] [-d] [-U] [-P] [-f]
                      [--file-per-object] [--data-only | --schema-and-data]
                      [--script-create | --script-drop | --script-drop-create]
                      [--target-server-version {2005,2008,2008R2,2012,2014,2016,vNext,AzureDB,AzureDW}]
                      [--target-server-edition {Standard,Personal,Express,Enterprise,Stretch}]
                      [--include-objects [[...]]] [--exclude-objects [[...]]]
                      [--include-schemas [[...]]] [--exclude-schemas [[...]]]
                      [--include-types [[...]]] [--exclude-types [[...]]]
                      [--ansi-padding] [--append] [--check-for-existence] [-r]
                      [--convert-uddts] [--include-dependencies]
                      [--exclude-headers] [--constraint-names]
                      [--unsupported-statements]
                      [--disable-schema-qualification] [--bindings]
                      [--collation] [--exclude-defaults]
                      [--exclude-extended-properties] [--logins]
                      [--object-permissions] [--owner]
                      [--exclude-use-database] [--statistics]
                      [--change-tracking] [--exclude-check-constraints]
                      [--data-compressions] [--exclude-foreign-keys]
                      [--exclude-full-text-indexes] [--exclude-indexes]
                      [--exclude-primary-keys] [--exclude-triggers]
                      [--exclude-unique-keys] [--display-progress]
                      [--enable-toolsservice-logging] [--version]

Microsoft SQL Server Scripter Command Line Tool. Version 1.0.0a23

optional arguments:
  -h, --help            show this help message and exit
  --connection-string   Connection string of database to script. If connection
                        string and server are not supplied, defaults to value
                        in environment variable
                        MSSQL_SCRIPTER_CONNECTION_STRING.
  -S , --server         Server name.
  -d , --database       Database name.
  -U , --user           Login ID for server.
  -P , --password       If not supplied, defaults to value in environment
                        variable MSSQL_SCRIPTER_PASSWORD.
  -f , --file-path      File to script out to or directory name if scripting
                        file per object.
  --file-per-object     By default script to a single file. If supplied and
                        given a directory for --file-path, script a file per
                        object to that directory.
  --data-only           By default only the schema is scripted. if supplied,
                        generate scripts that contains data only.
  --schema-and-data     By default only the schema is scripted. if supplied,
                        generate scripts that contain schema and data.
  --script-create       Script object CREATE statements.
  --script-drop         Script object DROP statements.
  --script-drop-create  Script object CREATE and DROP statements.
  --target-server-version {2005,2008,2008R2,2012,2014,2016,vNext,AzureDB,AzureDW}
                        Script only features compatible with the specified SQL
                        Version.
  --target-server-edition {Standard,Personal,Express,Enterprise,Stretch}
                        Script only features compatible with the specified SQL
                        Server database edition.
  --include-objects [ [ ...]]
                        Database objects to include in script.
  --exclude-objects [ [ ...]]
                        Database objects to exclude from script.
  --include-schemas [ [ ...]]
                        Database objects of this schema to include in script.
  --exclude-schemas [ [ ...]]
                        Database objects of this schema to exclude from
                        script.
  --include-types [ [ ...]]
                        Database objects of this type to include in script.
  --exclude-types [ [ ...]]
                        Database objects of this type to exclude from script.
  --ansi-padding        Generates ANSI Padding statements.
  --append              Append script to file.
  --check-for-existence
                        Check that an object with the given name exists before
                        dropping or altering or that an object with the given
                        name does not exist before creating.
  -r, --continue-on-error
                        Continue scripting on error.
  --convert-uddts       Convert user-defined data types to base types.
  --include-dependencies
                        Generate script for the dependent objects for each
                        object scripted.
  --exclude-headers     Exclude descriptive headers for each object scripted.
  --constraint-names    Include system constraint names to enforce declarative
                        referential integrity.
  --unsupported-statements
                        Include statements in the script that are not
                        supported on the target SQL Server Version.
  --disable-schema-qualification
                        Do not prefix object names with the object schema.
  --bindings            Script options to set binding options.
  --collation           Script the objects that use collation.
  --exclude-defaults    Do not script the default values.
  --exclude-extended-properties
                        Exclude extended properties for each object scripted.
  --logins              Script all logins available on the server, passwords
                        will not be scripted.
  --object-permissions  Generate object-level permissions.
  --owner               Script owner for the objects.
  --exclude-use-database
                        Do not generate USE DATABASE statement.
  --statistics          Script all statistics.
  --change-tracking     Script the change tracking information.
  --exclude-check-constraints
                        Exclude check constraints for each table or view
                        scripted.
  --data-compressions   Script the data compression information.
  --exclude-foreign-keys
                        Exclude foreign keys for each table scripted.
  --exclude-full-text-indexes
                        Exclude full-text indexes for each table or indexed
                        view scripted.
  --exclude-indexes     Exclude indexes (XML and clustered) for each table or
                        indexed view scripted.
  --exclude-primary-keys
                        Exclude primary keys for each table or view scripted.
  --exclude-triggers    Exclude triggers for each table or view scripted.
  --exclude-unique-keys
                        Exclude unique keys for each table or view scripted.
  --display-progress    Display scripting progress.
  --enable-toolsservice-logging
                        Enable verbose logging.
  --version             show program's version number and exit
  ```
  
 ## PS Script
 ```
$SERVER="LOGANSQL"
$DATABASELIST = ("db1","db2","db3")
$OUTDIR="C:\LOGANSQL\Scripts"
$LOG=$OUTDIR+"\"+$SERVER+"_Scripts_log_"+(Get-Date).ToString("yyyyMMdd_hhmm")+".txt"

foreach ($DATABASE in $DATABASELIST) {

(Get-Date).ToString("u") + ": Start scripting for $DATABASE on $SERVER..." | Out-File -Append -FilePath $LOG

$DBOUTDIR=$OUTDIR+'\'+$DATABASE

if(Test-Path -Path $DBOUTDIR){
  Get-ChildItem -Path $DBOUTDIR -Include *.* -File -Recurse | foreach { $_.Delete()}
}
else {
  mkdir $DBOUTDIR
}

$ENV:MSSQL_SCRIPTER_CONNECTION_STRING="Server=$SERVER;Database=$DATABASE;Trusted_Connection=True;"
$ENV:MSSQL_SCRIPTER_CONNECTION_STRING | Out-File -Append -FilePath $LOG

mssql-scripter --file-path $DBOUTDIR --file-per-object --script-drop-create  --display-progress 

"Scripting End for $DATABASE on $SERVER..."+(Get-Date).ToString("yyyyMMdd_hhmm") | Out-File -Append -FilePath $LOG
}
 ```
 # Create SQL Git Repository on Local
```
## On Server
## 0. Git Init
git init LoganSQLGitRepos.git --bare

## From Client
## 1. Git Clone
## git clone <path_to_your_server>
git clone \\myhost\gitserver\LoganSQLGitRepos.git

Cloning into 'LoganSQLGitRepos'...
warning: You appear to have cloned an empty repository.
done.

## 2. Git Add
## copy whatever sql folders and Git Add
cd .\LoganSQLGitRepos
git add *.*

## 3. Git Commit
git commit -m "initial commit"

## 4. Git Push
git push origin master
Counting objects: 1767, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (1767/1767), done.
Writing objects: 100% (1767/1767), 1.51 MiB | 891.00 KiB/s, done.
Total 1767 (delta 602), reused 0 (delta 0)
remote: Resolving deltas: 100% (602/602), done.
To //myhost/gitserver/LoganSQLGitRepos.git
 * [new branch]      master -> master

```
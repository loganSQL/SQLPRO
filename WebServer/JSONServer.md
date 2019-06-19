# JSON SERVER
## My Fake JSON Server From typicode.com
### [My-json-server.typicode.com/typicode/demo](https://my-json-server.typicode.com/typicode/demo)
### [LoganSQL/SQLPRO](http://my-json-server.typicode.com/logansql/sqlpro/posts)
* [posts](http://my-json-server.typicode.com/logansql/sqlpro/posts) [/1](http://my-json-server.typicode.com/logansql/sqlpro/posts/1)
* [comments](http://my-json-server.typicode.com/logansql/sqlpro/comments) [/1](http://my-json-server.typicode.com/logansql/sqlpro/comments/1)
* [profile](http://my-json-server.typicode.com/logansql/sqlpro/profile)
* [db](http://my-json-server.typicode.com/logansql/sqlpro/db)
### [Typicode/demo](https://github.com/typicode/demo) 
* [Demo](https://my-json-server.typicode.com/typicode/demo)

## JSON-SERVER
### [Install Node.JS](https://nodejs.org/en/download/)
nodejs – json-server is built on top of nodejs.

### Install JSON Server
```
npm install -g json-server
```
### Create a db.json file with some data
```
{
  "posts": [
    { "id": 1, "title": "json-server", "author": "logansql" }
  ],
  "comments": [
    { "id": 1, "body": "some comment", "postId": 1 }
  ],
  "profile": { "name": "logansql" }
}
```
### Start JSON Server
```
json-server --watch db.json
```
```
PS C:\logan\git\sqlpro\WebServer> json-server --watch db.json

  \{^_^}/ hi!

  Loading db.json
  Done

  Resources
  http://localhost:3000/posts
  http://localhost:3000/comments
  http://localhost:3000/profile

  Home
  http://localhost:3000

  Type s + enter at any time to create a snapshot of the database
  Watching...

GET /posts 200 9.358 ms - 77
GET /comments 200 4.015 ms - 68
GET /profile 200 4.203 ms - 24
```

### New JSON File (db.json)
This file contains the data which should be exposed by the REST API for objects contained in JSON structure CRUD endpoints are created automatically.
```
{
  "movies": [
    {"id": 1, "name": "The Godfather", "director":"Francis Ford Coppola", "rating": 9.1},
    {"id": 2, "name": "Casablanca", "director": "Michael Curtiz", "rating": 8.8}
  ]
}
```
```
PS C:\logan\git\sqlpro\WebServer> json-server --watch db.json

  \{^_^}/ hi!

  Loading db.json
  Done

  Resources
  http://localhost:3000/movies

  Home
  http://localhost:3000

  Type s + enter at any time to create a snapshot of the database
  Watching...

GET /movies 200 11.429 ms - 211
```
## Powershell Invoke-WebRequest
```
PS C:\logan>  $PSVersionTable.PSVersion

Major  Minor  Build  Revision
-----  -----  -----  --------
5      1      16299  820


PS C:\logan> Get-Alias -Definition Invoke-WebRequest | Format-Table -AutoSize

CommandType Name                      Version Source
----------- ----                      ------- ------
Alias       curl -> Invoke-WebRequest
Alias       iwr -> Invoke-WebRequest
Alias       wget -> Invoke-WebRequest


PS C:\logan> Invoke-WebRequest -Uri  http://localhost:3000/movies
...
S C:\logan> Invoke-WebRequest -Uri  http://localhost:3000/movies |select-object -ExpandProperty Content
[
  {
    "id": 1,
    "name": "The Godfather",
    "director": "Francis Ford Coppola",
    "rating": 9.1
  },
  {
    "id": 2,
    "name": "Casablanca",
    "director": "Michael Curtiz",
    "rating": 8.8
  }
]
PS C:\logan> curl http://localhost:3000/movies |select-object -ExpandProperty Content
[
  {
    "id": 1,
    "name": "The Godfather",
    "director": "Francis Ford Coppola",
    "rating": 9.1
  },
  {
    "id": 2,
    "name": "Casablanca",
    "director": "Michael Curtiz",
    "rating": 8.8
  }
]

```

## 
## [Install curl](https://curl.haxx.se/download.html)
curl is a command line tool to transfer data to or from a server, using any of the supported protocols (HTTP, FTP, IMAP, POP3, SCP, SFTP, SMTP, TFTP, TELNET, LDAP or FILE)
curl can test the routes of your mock server.

If you have GIT for Windows installed, curl.exe is at 'C:\Program Files\Git\mingw64\bin' already
```
PS C:\logan> cd 'C:\Program Files\Git\mingw64\bin\'
PS C:\Program Files\Git\mingw64\bin> .\curl.exe -X GET http://localhost:3000/movies
[
  {
    "id": 1,
    "name": "The Godfather",
    "director": "Francis Ford Coppola",
    "rating": 9.1
  },
  {
    "id": 2,
    "name": "Casablanca",
    "director": "Michael Curtiz",
    "rating": 8.8
  }
]
PS C:\logan\git\sqlpro\WebServer> get-alias curl

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Alias           curl -> Invoke-WebRequest

PS C:\logan\git\sqlpro\WebServer> set-alias -Name gitcurl -Value 'C:\Program Files\Git\mingw64\bin\curl.exe'
PS C:\logan\git\sqlpro\WebServer> get-alias gitcurl

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Alias           gitcurl -> curl.exe


PS C:\logan\git\sqlpro\WebServer> gitcurl -X GET http://localhost:3000/movies?id=1
[
  {
    "id": 1,
    "name": "The Godfather",
    "director": "Francis Ford Coppola",
    "rating": 9.1
  }
]
```
## POST request
### PS Invoke-RestMethod
POST request for HTTP is used for creating new entities
```
$JSON = @'
{"id": 3,
 "name": "Inception",
 "director": "Christopher Nolan",
 "rating": 9.0
}
'@

Invoke-RestMethod -Uri "http://localhost:3000/movies" -Method Post -Body $JSON -ContentType "application/json"

gitcurl http://localhost:3000/movies?id=3

$JSON = @'
{"id": 4,"name": "Inception","director": "Christopher Nolan","rating": 5}
'@

Invoke-RestMethod -Uri "http://localhost:3000/movies" -Method Put -Body $JSON -ContentType "application/json"

gitcurl -H 'Content-Type: application/json' -X PUT -d '{"id": 3,"name": "Inception","director": "Christopher Nolan","rating": 5}' http://localhost:3000/movies


$JSON = @{"id": 3,
 "name": "Inception",
 "director": "Christopher Nolan",
 "rating": 9.0
}
{"id": 6,"name": "Inception","director": "Christopher Nolan","rating": 7}
'@

$params = @{
    Uri         = 'http://localhost:3000/movies'
    Method      = 'PUT'
    Body        = $JSON
    ContentType = 'application/json'
}
Invoke-RestMethod @params

$response = Invoke-RestMethod 'http://localhost:3000/movies'

# hash table has no order, you need to use the [ordered] type adapter
$movie = [ordered]@{
    id      =   '3'
    name    =   'Inception'
    director=   'Christopher Nolan'
    rating  =   '9.0'
}
$json = $movie | ConvertTo-Json
$response = Invoke-RestMethod 'http://localhost:3000/movies' -Method Post -Body $json -ContentType 'application/json'


# update using PUT
$movie = [ordered]@{
    id      =   '3'
    name    =   'Inception'
    director=   'Christopher Nolan'
    rating  =   '9.8'
}

$json = $movie | ConvertTo-Json
$response = Invoke-RestMethod 'http://localhost:3000/movies/3' -Method Put -Body $json -ContentType 'application/json'
$response

# delete
$response = Invoke-RestMethod 'http://localhost:3000/movies/3' -Method Delete

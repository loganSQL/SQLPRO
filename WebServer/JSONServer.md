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
  "employees": [
    {
      "id": 1,
      "first_name": "Larry",
      "last_name": "Thomas",
      "email": "Larry@logansql.com"
    },
    {
      "id": 2,
      "first_name": "Marry",
      "last_name": "Lee",
      "email": "marry@logansql.com""
    },
    {
      "id": 3,
      "first_name": "Nick",
      "last_name": "Shen",
      "email": "Nick@logansql.com""
    }
  ]
}
```
```
PS C:\logan\git\sqlpro\WebServer> json-server --watch db.json

  \{^_^}/ hi!

  Loading db.json
  Done

  Resources
  http://localhost:3000/employees

  Home
  http://localhost:3000

  Type s + enter at any time to create a snapshot of the database
  Watching...

GET /employees 200 12.013 ms - 325
GET /employees/1 200 5.431 ms - 96
GET /employees/3 200 5.186 ms - 92
GET /employees 200 3.101 ms - 325
```
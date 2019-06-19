<#
REST APIs allow developers to interact with various services over HTTP/HTTPS and 
follow a common methodology of using methods to read and manipulate information. 
They return information in a standard way, typically through JavaScript Object Notation (JSON). 
The Invoke-RestMethod cmdlet is built with REST in mind. 
It allows the user to invoke various methods for web service APIs and easily parse the output.
#>
<#
Powershell:
    Invoke-WebRequest
    invoke-RestMethod
    ConvertTo-Json
    ConvertFrom-Json
    ConvertTo-html
    ConvertFrom-html

#>

<#
All REST APIs have a base URL and one or more endpoints
#>

<#
The Invoke-WebRequest command performs a similar function by sending HTTP verbs to web services
#>
Get-Alias -Definition Invoke-WebRequest | Format-Table -AutoSize

curl http://localhost:3000/movies

(invoke-webrequest -Uri 'http://localhost:3000/movies').content

Invoke-WebRequest -Uri  http://localhost:3000/movies |select-object -ExpandProperty Content

<#
invoke-RestMethod command's biggest advantages is its native parsing ability. 
Invoke-RestMethod understands that a URI is REST and will probably return JSON. When the API does return JSON, 
Invoke-RestMethod will parse the JSON and return useful PowerShell objects. 
#>

Invoke-RestMethod -Uri 'http://localhost:3000/movies'

<#
The Invoke-RestMethod command allows you to pass OAuth tokens and other information the API needs via HTTP headers using the Headers parameter. 
Perhaps the REST API is set up to accept OAuth tokens using the command Authorization key. 
#>

# This command doesn't just retrieve information via APIs using the HTTP GET method sent by default.
Invoke-RestMethod -Uri 'https://cat-fact.herokuapp.com/facts' -Headers @{ 'Authentication' = 'Bearer xxxxxxxxxxxxxxxx' }

Invoke-RestMethod -Uri 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=MSFT&apikey=demo'
Invoke-RestMethod -Uri 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=demo'
Invoke-RestMethod -Uri 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=BA&apikey=demo'
Invoke-RestMethod -Uri 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo'
Invoke-RestMethod -Uri 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=CAD&to_currency=USD&apikey=demo'

<#
We can use many different HTTP methods like POST, PATCH, PUT, and UPDATE as well. 
We simply need to specify the method via the Method parameter and then provide an HTTP body using the Body parameter.
#>

<#
    POST
#>
# saved our JSON payload in a variable called $JSON
# POST request for HTTP is used for creating new entities
$JSON = @'
{"id": 4,
 "name": "Call Me by Your Name ",
 "director": "Luca Guadagnino",
 "rating": 8.5
}
'@

Invoke-RestMethod -Uri "http://localhost:3000/movies" -Method Post -Body $JSON -ContentType "application/json"

Invoke-RestMethod -Uri "http://localhost:3000/movies"

# JSON Payload
$JSON = @'
{"id": 6,
 "name": "Catch Me If You Can",
 "director": "Steven Spielberg",
 "rating": 9.5
}
'@
$params = @{
    Uri         = 'http://localhost:3000/movies'
    Method      = 'POST'
    Body        = $JSON
    ContentType = 'application/json'
}
Invoke-RestMethod @params
Invoke-RestMethod -Uri "http://localhost:3000/movies"


<#
    Put
#>
# Modify the rating to 5 from 9
# hash table has no order, you need to use the [ordered] type adapter
$movie = [ordered]@{
    id      =   '3'
    name    =   'Inception'
    director=   'Christopher Nolan'
    rating  =   '5'
}
$json = $movie | ConvertTo-Json
$response = Invoke-RestMethod 'http://localhost:3000/movies/3' -Method Put -Body $json -ContentType 'application/json'
$response
Invoke-RestMethod -Uri "http://localhost:3000/movies"

<# 
    Delete
#>
$response = Invoke-RestMethod 'http://localhost:3000/movies/5' -Method Delete

<#
    ConvertTo-Json
#>

$body = @{
    "UserSessionId"="12345678"
    "OptionalEmail"="lanakane@test.com"
} | ConvertTo-Json
    
$header = @{
    "Accept"="application/json"
    "connectapitoken"="29a696c910b441989e367afa23c3c31c"
}
    
$params = @{
    Uri = 'http://NZL075/WSVistaWebClient/RESTLoyalty.svc/member/search'
    Headers = $header
    Method = 'POST'
    Body = $body
    ContentType = 'application/json'
    }
    
Invoke-RestMethod @params | Format-List
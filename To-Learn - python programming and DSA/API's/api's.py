#API -- Application Programming Interface

#API allows two applications to communicate

#client
#   ↓
#  api
#   ↓
#server

#eg
#Suppose a weather app needs temperature

#app sends request to weather API

#Weather server:processes request sends weather data back

#this entire communication happens through api

#without api communication of any type between two system are not done properly



#REST APIs

#this is a style of api used widely today

#REST = Representational State Transfer

# follows a client ↔ server architecture.

#But practically  REST means structured HTTP-based APIs

#REST APIs Use
#URLs
#HTTP methods
#JSON data
#status codes

#reat Resources are represented by URLs

#https://api.example.com/users

#https:// --->	protocol
#api.example.com	 ---> server/domain
#/users  --->	resource endpoint

#REST APIs use HTTP methods to describe action.
#it uses

# GET    --->  fetch data
# POST   --->  create/send data
# PUT    --->  update data
# DELETE --->  remove data


#Python App
#     ↓ HTTP Request
#Server/API
#     ↓ HTTP Response
#Python App

#GET

#GET is used to fetch data from server

# in python requests are used for fetching data from urls


import requests

response = requests.get(
    "https://api.example.com/users"
)

#Python app sends HTTP GET request to server

#Server Receives Request
#Server processes:
#URL
#authentication
#database query
#business logic

#Server Sends Response
#Server returns:
#status code
#headers
#data


print(response.status_code) #returns status code

print(response.text)  #returns raw string data


#json() is more preferred in modern api's
data = response.json()

print(data)

#json automatically does deserialization
#JSON String
#      ↓ response.json()
#Python Dictionary



#Query Parameters

#Used for:
#searching
#filtering
#pagination


#/users?id=10 ---> "Give user whose id is 10"

url = "https://api.example.com/users"

params = {"id": 10}

responseA = requests.get(
    url,
    params=params         #python automatically builds  /users?id=10
)

params = {
    "page": 2,
    "limit": 10
}                       #mutliple params internally ---> ?page=2&limit=10


#POST requests

#used for send/create data

data = {
    "name": "Aravind",
    "age": 21
}

response = requests.post(
    "https://api.example.com/users",
    json=data
)

#json=data means convert Python dictionary → JSON automatically


#Client sends POST request + JSON body

#Server receives data

#Server may
#validate
#store in database
#process business logic

#Server sends response


#Python Dictionary
#      ↓
#JSON Serialization
#      ↓
#HTTP Request Body
#     ↓
#Server


#PUT REQUEST

#used for update existing resource

data = {
    "name": "Aravind Updated"
}

responseB = requests.put(
    "https://api.example.com/users/1",
    json=data
)

#update user with id 1


#DELETE REQUEST

#used to remove resources

responseC = requests.delete(
    "https://api.example.com/users/1"

)

#delete user 1


#HTTP STATUS CODES

statuscode = response.status_code

#Code	Meaning
#200	success
#201	created
#400	bad request
#401	unauthorized
#403	forbidden
#404	not found
#500	server error


#Headers

#contains metadata about request/response

#authentication tokens
#content type
#caching info

headers = {
    "Authorization": "Bearer TOKEN"
}

#sending headers
requests.get(
    url,
    headers=headers
)

#Authentication

#Many APIs require
#API keys
#tokens
#login credentials

headers = {
    "Authorization": "Bearer abc123"
}


#rest api's full flow
#Python App
#     ↓
#HTTP Request
#(GET/POST/etc)
#     ↓
#REST API Server
#     ↓
#Database/Logic
#     ↓
#HTTP Response
#(JSON)
#     ↓
#Python App





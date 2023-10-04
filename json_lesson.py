import json

data= '{"name":"win","email":"win@gmail.com","password":"123win"}'
myapi=json.loads(data)
print(myapi)
print(type(myapi))
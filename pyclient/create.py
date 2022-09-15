import requests
response=requests.get("http://localhost:5000/api/create/",data={"name":"cake","price":340.0})
print(response.json())
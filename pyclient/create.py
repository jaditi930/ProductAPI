import requests
response=requests.post("http://localhost:5000/api/create/",json={"name":"cake","price":340.0})
print(response.json())
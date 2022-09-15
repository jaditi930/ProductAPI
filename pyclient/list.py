import requests
response=requests.get("http://localhost:5000/api/detail/")
print(response.json())
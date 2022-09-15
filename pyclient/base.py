import requests
response=requests.get("http://localhost:5000/api/")
#print(response.text)
print(response.json())

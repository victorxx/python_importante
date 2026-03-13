import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

res = requests.get(url)
print(res.status_code)
print(res.json())


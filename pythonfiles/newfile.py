import requests
r = requests.get("http://localhost:8000/blog/posts/").json()
print(r)

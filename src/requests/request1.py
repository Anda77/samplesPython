import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)

print(x.status_code)

res = requests.get("https://urlscan.io")
print(res.status_code)

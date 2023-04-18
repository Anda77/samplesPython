import certifi
import requests
import urllib3

urllib3.disable_warnings()
print(certifi.where())

session = requests.Session()
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    # "cookie": "Cookie: Something",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0"
}
# session.cookies.add_cookie_header(session)
session.headers = headers
# https://reqbin.com/echo/get/json
a = session.get("https://google.com/", allow_redirects=True)
# works
a = session.get("https://reqbin.com/echo/get/json", verify=True)
print(a.reason)

print(a)

print(a.status_code)
a = session.get("https://reqbin.com/echo/get/json", verify=False)
print(a.reason)

print(a)

print(a.status_code)
a = session.get("https://reqbin.com/echo/get/json",
                verify="C:\\Users\\andad\\OneDrive\\Desktop\\BaltimoreCyberTrustRoot.crt")
print(a.reason)

print(a)

print(a.status_code)

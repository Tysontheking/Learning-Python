import requests

data = {"username":"text","password":'test1234'} #data = {"key": "value"}

r = requests.post("https://httpbin.org/post",data)
# print(r.text)

try:
    print(data["username"])
    print(data["password"])
except KeyError:
    print("KeyError occurred")
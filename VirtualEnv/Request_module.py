import requests

req = requests.get("https://api.github.com/users/kingofhero")

with open("Kingofhero.txt","w") as f:
    f.write(req.text)


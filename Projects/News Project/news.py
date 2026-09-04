import requests

query = input("What kind of news are you looking for? ")
# query = "tesla"
api_key = "fd567bb4d94645caa641496c4f64cca4"

Url = f"https://newsapi.org/v2/everything?q={query}&from=2026-08-03&sortBy=publishedAt&apiKey={api_key}"

# print(Url)

data = requests.get(Url).json()
articles = data["articles"]
print(articles)

for index,article in enumerate(articles):
    print(f"{index+1, article["title"]} and {article["url"]}")
    print("\n**************************************\n")

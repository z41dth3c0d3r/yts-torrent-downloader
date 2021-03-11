import requests

yts_serach = requests.get("https://yts.mx/browse-movies")

print(yts_serach.content)
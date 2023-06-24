# import requests

# url = "https://unofficial-cricbuzz.p.rapidapi.com/players/get-batting"

# querystring = {"playerId":"6640"}

# headers = {
# 	"X-RapidAPI-Key": "7342f3af94msh458c6999db3a295p1672a0jsn1d4f7254e3ca",
# 	"X-RapidAPI-Host": "unofficial-cricbuzz.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())

import requests

url = "https://unofficial-cricbuzz.p.rapidapi.com/players/search"

querystring = {"plrN":"*"}

headers = {
	"X-RapidAPI-Key": "7342f3af94msh458c6999db3a295p1672a0jsn1d4f7254e3ca",
	"X-RapidAPI-Host": "unofficial-cricbuzz.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

json = response.json()


print(response.json())
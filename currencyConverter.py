import requests

# Where BRL is the base currency you want to use
url = 'https://api.exchangerate-api.com/v4/latest/BRL'


# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print(data)

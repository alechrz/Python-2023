import requests
from pprint import pprint

url = "https://api.chucknorris.io/jokes/random"
response = requests.request(method="GET", url=url)

pprint(response.json())

print()
print(25*"*")
print()
print(response.json()['value'])

url="https://restcountries.com/v3.1/name/Poland?fullText=true"
response = requests.request(method="GET", url=url)

response=response.json()[0]
pprint(response)
print('name:',response['name']['common'], 'capital:',response['capital'][0],'area:' ,response['area'], 'languages:', response['languages']['pol'], 'currencies', *response['currencies'].keys())



import requests
import sys
country = sys.argv[1]
url = f"https://restcountries.com/v3.1/name/{country}?fullText=true"
response = requests.request(method="GET", url=url)

data = response.json()[0]


print(f"Capital:    {data['capital'][0]}")
print(f"Population: {data['population']}")
print(f"Area:       {data['area']}")
print(f"Flag:       {data['flags']['alt']}")
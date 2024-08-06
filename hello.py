import requests, json

word = 'worple'

url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
print(url)
exit(0)
print('one')
response = requests.get(url=url)

print(response)

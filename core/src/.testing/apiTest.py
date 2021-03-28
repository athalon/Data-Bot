import requests
from random import randint

'''
TODO: Start implimenting the api commands. API lists:
API_list.md
https://apilist.fun/
https://some-random-api.ml/
'''

request = requests.get('https://api.publicapis.org/entries')
request_dict = request.json()

valid_entries = {}

print(len(request_dict['entries']))

for entry in request_dict['entries']:
    if entry['Auth'] == "":
        valid_entries['id_'+str(randint(1, 1000))] = entry

with open('./core/src/.testing/API_list.md', 'a', encoding='utf-8') as f:
    for entry in valid_entries:
        f.write(f"`Name:` {valid_entries[entry]['API']}, `Description:` {valid_entries[entry]['Description']}, [Link] ({valid_entries[entry]['Link']})\n")

print("API sorting and validation done!")
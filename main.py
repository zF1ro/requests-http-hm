"""
Задача №1
Кто самый умный супергерой?
Есть API по информации о супергероях с информацией по всем супергероям. Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.
"""
import requests
import json

url = "https://akabab.github.io/superhero-api/api/all.json"
cdn_url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api"

response = requests.get(url)
#print(response.status_code)
if 200 <= response.status_code < 300:
    with open("superheroes.json", "w") as file:
        file.write(response.text)

list_for_iq_test = ['Hulk', 'Captain America', 'Thanos']
dict_for_iq_test = {}
with open("superheroes.json", "r") as file:
    data = json.load(file)
    for superhero in data:
        if superhero["name"] in list_for_iq_test:
            dict_for_iq_test[superhero["name"]] = superhero["powerstats"]["intelligence"]
hero_with_best_iq = max(dict_for_iq_test)

print(hero_with_best_iq)
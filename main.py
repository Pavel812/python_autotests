import requests
token = "e55b880909be02d66d1fb64aa7c02c0c"

'''newpokemons = requests.post('https://api.pokemonbattle.me:9104/pokemons',
                          json = {
    
    "name": "qastudio",
    "photo": "https://dolnikov.ru/pokemons/albums/007.png"

}, headers = {"Content-type":"application/json","trainer_token" : token,})

print(newpokemons.text)

if newpokemons.status_code == 200: 
    print('not bad!')
else:
    print('bad!')'''




'''changenamepokemons = requests.put('https://api.pokemonbattle.me:9104/pokemons',
                          json = {
    "pokemon_id": "12552",
    "name": "QASTUDIOTOP",
    "photo": "https://dolnikov.ru/pokemons/albums/004.png"
},
headers = {"Content-type":"application/json","trainer_token" : token,})
print(changenamepokemons.text)

if changenamepokemons.status_code == 200: 
    print('not bad!')
else:
    print('bad!')'''




pokemoninpokeball = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball',
                          json = {
    "pokemon_id": "12552"
},
headers = {"Content-type":"application/json","trainer_token" : token,})

print(pokemoninpokeball.text)

if pokemoninpokeball.status_code == 200: 
    print('not bad!')
else:
    print('bad!')







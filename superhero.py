import requests


def superhero():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url).json()
    intelligence_hero = {}
    for hero in response:
        if hero['name'] == 'Hulk' or hero['name'] == 'Captain America' or hero['name'] == 'Thanos':
            intelligence_hero[hero['name']] = hero['powerstats']['intelligence']
    the_most_intelligence_hero = sorted(intelligence_hero.items(), reverse=True)
    print(the_most_intelligence_hero[0][0])


superhero()
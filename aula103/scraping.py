import requests
from bs4 import BeautifulSoup

url = 'https://betteranime.net/'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for ultimos_lancamentos in html.select('.last-release'):
    for anime in ultimos_lancamentos.select('article'):
        titulo = anime.select_one('h3').text
        episodio = anime.select_one('h4').text
        tempo = anime.find_all('span')[2].text

        print(titulo, episodio, tempo, sep=' | ')

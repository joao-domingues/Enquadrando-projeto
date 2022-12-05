from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

page = urlopen ("https://letterboxd.com/luccaleal/list/filmes-do-enquadrando/detail/")
soup = BeautifulSoup(page, 'html.parser')
filmes = soup.find(class_='js-list-entries poster-list -p70 film-list clear film-details-list')
filmes_itens = filmes.find_all('h2')
filmess = []
for filmes in filmes_itens:
    names = filmes.contents[0].string
    filmess.append(names)

anos = []
for filmes in filmes_itens:
    names = filmes.contents[-1].string
    anos.append(names)


df = pd.DataFrame()
df['filmes'] = filmess
df['ano'] = anos
df.to_csv('C:/Users/Joao/enquadrando/letterboxd.csv', index=False, sep=';', header=False)
from email import header
from pdb import post_mortem
import pandas as pd
import numpy as np
from urllib.request import urlopen
import json
import urllib


df = pd.read_csv('C:/Users/Joao/enquadrando/letterboxd.csv', sep=';', header=None)
df.columns = ['nome', 'ano']
df['movie_link'] = np.nan
df['id'] = np.nan
df['poster_link'] = np.nan
df = df.replace(' ', '%20', regex=True)
base = 'https://api.themoviedb.org/3/search/movie?api_key='
api = '62837be5d9c3e91a14b19abfd99a0368'
meio = '&language=en-US&query='
fim = '&page=1&include_adult=false&year='
df['movie_link']=df['movie_link'].fillna(base + api + meio + df['nome']+ fim +df.ano.astype(str))

for index, row in df.iterrows():
    tmdb = urlopen(df['movie_link'][index]).read()
    a = tmdb.decode("utf-8")
    a = json.loads(a)
    movie_id = a['results'][0]['id']
    poster = a['results'][0]['poster_path']
    df.loc[index, 'id'] = movie_id
    df.loc[index,'poster_link'] = poster

df['poster_link']= 'https://image.tmdb.org/t/p/original'+df['poster_link'].astype(str)
df = df.replace('%20', ' ', regex=True)

x=1
for item in df['poster_link']:
    urllib.request.urlretrieve(item, 'C:/Users/Joao/enquadrando/posters/' + str(x) + '.jpeg')
    x+=1

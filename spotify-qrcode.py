# spotiPY pra pegar os episodios do enquadrando
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import json
import csv
import pandas as pd
import numpy as np
import urllib

# setting o environment
os.environ['SPOTIPY_CLIENT_ID'] = 'b590132ceacf4d6cba0781260348eb56'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'f99ce5525c6c411692d2cf060ab78a6d'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost'

# processo de OAuth, vai abrir uma página pra confirmar
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
sp.trace = False

# pegar a lista de episodios e fazer o dump pra dar pra ler
a = sp.show_episodes('6fdTAqzSl39E1PN6NuJr29', '50', '0', 'BR')


# criando estrutura pra salvar os resultados
a_dict = {
    'items': [],
}


# iterando cada episodio pra dentro do a_dict
for item in a['items']:
    item_dict = {
        item['name'],
        item['id']
    }
    a_dict['items'].append(item_dict)

df = pd.DataFrame(a_dict['items'])
df.columns = ['Nome','Code']
df.loc[df['Code'].str.startswith('En'), ['Nome', 'Code']] = df.loc[df['Code'].str.startswith('En'), ['Code', 'Nome']].values
df["Links"] = np.nan
df['Links'] = df['Links'].fillna('https://scannables.scdn.co/uri/plain/png/000000/white/640/spotify:episode:' + df['Code'])

df = df.reindex(index=df.index[::-1])
df.to_csv('C:/Users/Joao/enquadrando/podcast.csv', header=False, index=False, sep=';')

x=1
for item in reversed(df['Links']):
    urllib.request.urlretrieve(item, 'C:/Users/Joao/enquadrando/spotify/' + str(x) + '.png')
    x+=1
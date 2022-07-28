import pandas as pd
import spacy
from matplotlib import pyplot as plt
import json
import requests

nlp = spacy.load('en_core_web_sm')

# prva tacka
df1 = pd.read_csv('C:\\Users\\Korisnik\\Desktop\\intens zadatak\\descriptive_attributes.csv')
df2 = pd.read_csv('C:\\Users\\Korisnik\\Desktop\\intens zadatak\\numeric_atributes.csv', low_memory=False)
output1 = pd.merge(df1, df2,
                   on='movieID',
                   how='inner')

# druga tacka
print('Broj redova u kojima nije popunjena vrednost kolone isGood: ', output1['isGood'].isna().sum())

# treca tacka
output1['averageRating'] = output1['averageRating'].fillna(0)

# cetvrta tacka
df = output1.loc[(output1['startYear'] > 2000) & (output1['averageRating'] > 3)]
print('Broj redova u kojima je godina početka emitovanja iznad 2000 i prosečna ocena gledalaca iznad 3: ', len(df))
print(df)

# peta tacka - histogram
plt.title("Histogram")
plt.xlabel("prosečna ocena")
plt.ylabel("broj elemenata")
plt.hist(output1.averageRating, bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# sesta tacka
new_df = output1.groupby('titleType')['averageRating'].mean()
print('Prosečna vrednost ocene za svaku kategoriju videa:')
print(new_df)

# sedma tacka - spacy 'similarity'
title = nlp("The French Connection")
for i in range(0, len(output1['originalTitle'])):
    new_title = nlp(output1['originalTitle'].values[i])
    output1.loc[i, 'similarity'] = title.similarity(new_title)

print(output1.sort_values(by='similarity', ascending=False).head(10))

# osma tacka
tabela = pd.DataFrame()
k = 0
for i in range(0, len(output1['originalTitle'])):
    new_title = nlp(output1['originalTitle'].values[i])
    for token in new_title:
      if((token.pos_ != 'PUNCT') & (token.pos_ != 'SYM') & (token.is_digit == 0)):
        ind = 0
        word = token.lemma_
        for l in range(k):
          if(word == tabela['reci'].values[l]):
            tabela['broj'].values[l] = tabela['broj'].values[l] + 1
            ind = 1
            break
        if(ind == 0):
          tabela.loc[k, 'reci'] = word
          tabela.loc[k, 'broj'] = 1
          k = k + 1

tabela.to_csv('nova_tabela.csv')

# deveta tacka
r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
print(r.json()["bpi"]["USD"]["rate_float"])

import pandas as pd

# prva tacka
df1 = pd.read_csv('C:\\Users\\Korisnik\\Desktop\\intens zadatak\\descriptive_attributes.csv')
df2 = pd.read_csv('C:\\Users\\Korisnik\\Desktop\\intens zadatak\\numeric_atributes.csv', low_memory=False)
output1 = pd.merge(df1, df2,
                   on='movieID',
                   how='inner')
# druga tacka
print(output1['isGood'].isna().sum())
print(output1['averageRating'].isna().sum())
# treca tacka
# output1['averageRating'].fillna(0)
# for i in range(0,len(output1['averageRating'])):
#     if output1.iloc[i]['averageRating'] == None:
#         print(i)

# cetvrta tacka
df = output1.loc[(output1['startYear'] > 2000) & (output1['averageRating'] > 3)]
print(df)
print(len(df))

# peta tacka - histogram

# sesta tacka
new_df = output1.groupby('titleType')['averageRating'].mean()
# print(new_df)

# sedma tacka - spacy 'similarity'

# osma tacka
original_Title = output1.pop('originalTitle')
primary_Title = output1.pop('primaryTitle')
s = original_Title.str.split(expand=True)
t = s.stack()
r = t.reset_index(1, drop=True)
n = r.rename('originalTitle')
# print(n)

df3 = output1.join(n)
df3 = df3.reset_index(drop=True)
df3 = df3.drop_duplicates(['movieID', 'originalTitle'])
df3 = df3.groupby('originalTitle', sort=False)
df3 = df3.agg('Totalcount', 'size')
df3 = df3.reset_index()
df3 = df3.rename(columns={'originalTitle': 'Word'})
print(df3)
# print(output1.dtypes)
# print(output1.shape[0])
# print(len(output1))
# print(output1.info())
# print(output1.describe())
# print(output1['isGood'])
# slika = output1['averageRating']
# print(slika)
# slika.plot.hist()
# print(output1['isGood'].isna().sum())
# print(len(output1['isGood']))

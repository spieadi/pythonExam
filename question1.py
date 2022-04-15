import os
import pandas as pd

root = os.getcwd()
file = pd.read_csv(os.path.join(root,'Bordeaux_Metropole.csv'))
# df = pd.read_excel(os.path.join(root,'Realstate.xlsx'))
# df_bordeaux = pd.read_csv('dataset/Bordeaux_Metropole.csv')

def v(x):
    if x==33000 or x==33110 or x==33440:
        return x

post_code = file['code_postal'].apply(v)
df = pd.DataFrame(post_code)
df = df.dropna()
print(df)

for item in post_code:
    if item == 33000 or 33110 or 33440:
     data = file[(file['code_postal']==item) & (file['type_local']=='Appartement')]
     data = data[['valeur_fonciere', 'surface_relle_bati']]
     descriptive_stat = data.describe()
     descriptive_stat.to_csv('D:\MBS Semester 2\exam\data/' + str(item) + '.csv')

    
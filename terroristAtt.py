import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import seaborn as sns

plt.style.use('fivethirtyeight')

df = pd.read_csv('globalterror.csv', encoding = "ISO-8859-1")

df.rename(columns={'iyear':'Year','country_txt':'Country','nkill':'Killed','nwound':'Wounded','attacktype1_txt':'AttackType'}, inplace = True)
df=df[['Year','Country','Killed','Wounded','AttackType']].fillna(0)
print('Country with Highest Terrorist Attacks:',df['Country'].value_counts().index[0])
print('Maximum people killed in an attack are:',df['Killed'].max(),'that took place in',df.loc[df['Killed'].idxmax()].Country)



plt.subplots(figsize=(13,6))
sns.countplot('Year',data=df,palette='OrRd')
plt.xticks(rotation=90)
plt.title('Number Of Terrorist Activities Each Year')
plt.show()

plt.subplots(figsize=(13,6))
sns.countplot('AttackType',data=df,palette='dark',order=df['AttackType'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Attacking Methods by Terrorists')
plt.show()s

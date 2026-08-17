import pandas as pd

df = pd.read_csv('clientes_churn.csv')

df.info()
df.isnull().sum()
df.duplicated().sum()

df = df.drop_duplicates()
df['Plano'] = df['Plano'].fillna('Nao informado')
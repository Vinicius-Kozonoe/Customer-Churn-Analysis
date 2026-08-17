import pandas as pd

df = pd.read_csv('clientes_churn.csv')

df.info()
df.isnull().sum()
df.duplicated().sum()
import pandas as pd

df = pd.read_csv('clientes_churn.csv')

df.info()
df.isnull().sum()
df.duplicated().sum()

df = df.drop_duplicates()
df['Plano'] = df['Plano'].fillna('Nao informado')

df['Mensalidade'] = df.groupby('Plano')['Mensalidade'].transform(lambda x: x.fillna(x.median()))

print(df.isnull().sum())

bins = [0, 25, 35, 45, 55, 100]
labels = ['18-25', '26-35', '36-45', '46-55', '56+']
df['Faixa_Etaria'] = pd.cut(df['Idade'], bins=bins, labels=labels)

df['Faixa_Contrato'] = pd.cut(df['Tempo_Contrato_Meses'], bins=[0, 12, 24, 36, 48, 100],
                                labels=['0-12', '13-24', '25-36', '37-48', '49+'])

churn_plano = df.groupby('Plano')['Churn'].apply(lambda x: (x == 'Sim').mean())
print(churn_plano.sort_values(ascending=False))

churn_reclamacoes = df.groupby('Reclamacoes')['Churn'].apply(lambda x: (x == 'Sim').mean())
print(churn_reclamacoes)

churn_contrato = df.groupby('Faixa_Contrato')['Churn'].apply(lambda x: (x == 'Sim').mean())
print(churn_contrato)
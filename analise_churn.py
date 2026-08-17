import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('clientes_churn.csv')

df.info()
df.isnull().sum()
df.duplicated().sum()

# Tratar dados nulos 

df = df.drop_duplicates()
df['Plano'] = df['Plano'].fillna('Nao informado')

df['Mensalidade'] = df.groupby('Plano')['Mensalidade'].transform(lambda x: x.fillna(x.median()))

print(df.isnull().sum())

# Criação faixa etárias

bins = [0, 25, 35, 45, 55, 100]
labels = ['18-25', '26-35', '36-45', '46-55', '56+']
df['Faixa_Etaria'] = pd.cut(df['Idade'], bins=bins, labels=labels)

df['Faixa_Contrato'] = pd.cut(df['Tempo_Contrato_Meses'], bins=[0, 12, 24, 36, 48, 100],
                                labels=['0-12', '13-24', '25-36', '37-48', '49+'])

# Churn por ...

churn_plano = df.groupby('Plano')['Churn'].apply(lambda x: (x == 'Sim').mean())
print(churn_plano.sort_values(ascending=False))

churn_reclamacoes = df.groupby('Reclamacoes')['Churn'].apply(lambda x: (x == 'Sim').mean())
print(churn_reclamacoes)

churn_contrato = df.groupby('Faixa_Contrato')['Churn'].apply(lambda x: (x == 'Sim').mean())
print(churn_contrato)

churn_idade = df.groupby('Faixa_Etaria')['Churn'].apply(lambda x: (x == 'Sim').mean())
print(churn_idade.sort_values(ascending=False))

churn_regiao = df.groupby('Regiao')['Churn'].apply(lambda x: (x == 'Sim').mean())
print(churn_regiao.sort_values(ascending=False))

perfil_churn = df.groupby('Churn')[['Idade', 'Tempo_Contrato_Meses', 'Mensalidade', 'Reclamacoes', 'Chamados_Suporte']].mean()
print(perfil_churn)

# Gráficos

plt.figure(figsize=(8, 5))
churn_plano.sort_values(ascending=False).plot(kind='bar', color='steelblue')
plt.title('Taxa de Churn por Plano')
plt.ylabel('Taxa de churn')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('churn_por_plano.png')
plt.show()

plt.figure(figsize=(8, 5))
churn_regiao.sort_values(ascending=False).plot(kind='bar', color='darkorange')
plt.title('Taxa de Churn por Região')
plt.ylabel('Taxa de churn')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('churn_por_regiao.png')
plt.show()

plt.figure(figsize=(8, 5))
churn_idade.plot(kind='bar', color='seagreen')
plt.title('Taxa de Churn por Faixa Etária')
plt.ylabel('Taxa de churn')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('churn_por_idade.png')
plt.show()

plt.figure(figsize=(8, 5))
churn_contrato.plot(kind='bar', color='indianred')
plt.title('Taxa de Churn por Tempo de Contrato')
plt.ylabel('Taxa de churn')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('churn_por_contrato.png')
plt.show()

# Exporta o resultado

df.to_csv('clientes_churn_tratado.csv', index=False)
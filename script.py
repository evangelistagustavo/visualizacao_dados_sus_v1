import pandas as pd
import sqlite3

conn = sqlite3.connect('datasus.db')

df = pd.read_csv('prod_amb_sus_1.csv', sep=';', encoding='latin-1', skiprows=5)

df[['codigo_uf', 'nome_uf']] = df['UF'].str.split(' ', expand=True, n=1)
df = df.drop('UF', axis=1)
df = df.dropna(subset=['Qtd.aprovada'])

total_geral = df[df['codigo_uf'] == 'Total']
df = df[df['codigo_uf'] != 'Total']

df['percentual'] = (df['Qtd.aprovada'] / total_geral['Qtd.aprovada'].iloc[0] * 100)

df.to_sql('prod_amb_sus', conn, if_exists='replace', index=False)
total_geral.to_sql('total_geral', conn, if_exists='replace', index=False)

conn.close()


#Query de teste
conn = sqlite3.connect('datasus.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM prod_amb_sus LIMIT 5')
resultado = cursor.fetchall()
print(resultado)

#Query UFs com mais exames
conn = sqlite3.connect('datasus.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM prod_amb_sus ORDER BY "Qtd.aprovada" DESC LIMIT 5')
resultado = cursor.fetchall()   
print(resultado)
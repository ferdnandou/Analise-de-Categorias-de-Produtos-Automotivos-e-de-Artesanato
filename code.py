import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('categorias_produtos.csv')

# Explorar os dados
print(df.head())
print(df.info())
print(df.describe())

# Limpeza de dados
df = df.drop_duplicates()

# Análise por gráficos
# Gráfico de Barras: Quantidade de categorias em cada indústria
plt.figure(figsize=(10,6))
plt.bar(['Artesanato', 'Automotiva'], [len(df[df['category_name'].str.contains('Arts')]), len(df[df['category_name'].str.contains('Auto')])])
plt.xlabel('Indústria')
plt.ylabel('Quantidade de Categorias')
plt.title('Quantidade de Categorias por Indústria')
plt.show()

# Gráfico de Pizza: Proporção de cada categoria dentro de cada indústria
plt.figure(figsize=(10,6))
plt.pie([len(df[df['category_name'].str.contains('Arts')]), len(df[df['category_name'].str.contains('Auto')])], labels=['Artesanato', 'Automotiva'], autopct='%1.1f%%')
plt.title('Proporção de Categorias por Indústria')
plt.show()



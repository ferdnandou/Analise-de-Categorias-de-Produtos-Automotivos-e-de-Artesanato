# Análise de Categorias de Produtos

Este projeto realiza uma análise de dados de categorias de produtos com o uso das bibliotecas `pandas` e `matplotlib` em Python. O objetivo é explorar e visualizar a distribuição das categorias de produtos em duas indústrias: Artesanato e Automotiva.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:
- `pandas`
- `matplotlib`

Você pode instalá-las usando pip:

```bash
pip install pandas matplotlib
```

## Arquivos

- `categorias_produtos.csv`: Arquivo CSV contendo dados das categorias de produtos.

## Código

### Carregar e Explorar os Dados

O código carrega os dados do arquivo `categorias_produtos.csv` e realiza uma exploração inicial:

```python
import pandas as pd

# Carregar os dados
df = pd.read_csv('categorias_produtos.csv')

# Explorar os dados
print(df.head())
print(df.info())
print(df.describe())
```

### Limpeza de Dados

Os dados são limpos removendo duplicatas:

```python
df = df.drop_duplicates()
```

### Análise por Gráficos

1. **Gráfico de Barras: Quantidade de Categorias em Cada Indústria**

   Este gráfico mostra a quantidade de categorias de produtos em cada indústria.

   ```python
   import matplotlib.pyplot as plt

   plt.figure(figsize=(10,6))
   plt.bar(['Artesanato', 'Automotiva'], [len(df[df['category_name'].str.contains('Arts')]), len(df[df['category_name'].str.contains('Auto')])])
   plt.xlabel('Indústria')
   plt.ylabel('Quantidade de Categorias')
   plt.title('Quantidade de Categorias por Indústria')
   plt.show()
   ```

2. **Gráfico de Pizza: Proporção de Cada Categoria Dentro de Cada Indústria**

   Este gráfico mostra a proporção de categorias em cada indústria.

   ```python
   plt.figure(figsize=(10,6))
   plt.pie([len(df[df['category_name'].str.contains('Arts')]), len(df[df['category_name'].str.contains('Auto')])], labels=['Artesanato', 'Automotiva'], autopct='%1.1f%%')
   plt.title('Proporção de Categorias por Indústria')
   plt.show()
   ```

## Como Usar

1. Coloque o arquivo `categorias_produtos.csv` no mesmo diretório do script.
2. Execute o script Python para gerar e visualizar os gráficos.

```bash
python categorias_produtos.csv.py
```

import pandas as pd
import numpy as np
import dask.dataframe as dd

dir = 'C:\\Users\\spideryzarc\\Downloads\\'
# Carregando os dados csv.zip
prod = pd.read_csv(dir + 'producto_tabla.csv.zip', index_col='Producto_ID')
print(prod.head())
cliente = pd.read_csv(dir + 'cliente_tabla.csv.zip', index_col='Cliente_ID')
print(cliente.head())
town = pd.read_csv(dir + 'town_state.csv.zip', index_col='Agencia_ID')
print(town.head())

train = dd.read_csv(dir + 'train.csv.zip')
# print(train[train.Dev_uni_proxima>0].sample(1e-6))

#Gerar uma amostra menor de treino e salvar em um arquivo parquet.gz 
train_s = train.sample(frac=1e-4, random_state=42).compute()
train_s.to_parquet(dir + 'train_sample.parquet.gz', compression='gzip', index=False)


#Salvar dataset completo como parquet.gz
train.compute().to_parquet(dir + 'train.parquet.gz', compression='gzip', index=False)

#Carregar a amostra menor de treino para um DataFrame 
train_s = pd.read_csv(dir + 'train_sample.csv.gz', index_col='Unnamed: 0')

#drop clientes com apenas uma compra
v = train.Cliente_ID.value_counts()
v = v[v<=1]
train = train[~train.Cliente_ID.isin(v.index)]

#drop produtos com apenas uma compra
v = train.Producto_ID.value_counts()
v = v[v<=1]
train = train[~train.Producto_ID.isin(v.index)]

#drop agencias com apenas uma compra
v = train.Agencia_ID.value_counts()
v = v[v<=1]

#


# %%
import pandas as pd

# %%
df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()

# %%
df.shape

# %%
df.info(memory_usage='deep')

# %%
df.dtypes

# %%
renamed_columns = {"QtdePontos": "qtPontos",
                    "DescSistemaOrigem": "SistemaOrigem"}

df.rename(columns=renamed_columns, inplace=True)

# %%
df.head()

# %%
df[["idClientes", "qtPontos"]]

# %%
renamed_idClientes = {"idClienteS": "idClientes"}
df.rename(columns=renamed_idClientes, inplace=True)
# %%
df[['idClientes']]

# %%
df[["idClientes", "qtPontos"]].sample(5)

# %%
df.head()

# %%
df[['idClientes', 'IdTransacao', 'qtPontos']].head(5)

# %%
colunas = list(df.columns)
colunas.sort()

df = df[colunas]
df.head()

# %%
import pandas as pd

# %%
df = pd.read_csv('../data/transacao_produto.csv', sep=';')
df.head()

# %%
filtro = df['IdProduto'].isin([5, 11])
df[filtro]

# %%
clientes = pd.read_csv('../data/clientes.csv', sep=';')
clientes.sample(5)

# %%
clientes.shape
# %%
filtro = clientes['DtCriacao'].notna()
clientes[filtro].shape

# %%
filtro.shape
# %%
clientes['DtCriacao'].notna()
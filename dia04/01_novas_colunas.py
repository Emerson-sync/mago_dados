# %%
import pandas as pd

# %%
df = pd.read_csv('../data/clientes.csv', sep=';')
cresc = df.sort_values('DtCriacao')
# df.head(15)

# %%
df['qtdePontos'] + 100
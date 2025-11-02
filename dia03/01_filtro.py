# %%
import pandas as pd

# %%
df = pd.read_csv('../data/transacoes.csv', sep=';')
df.head()

# %%
brinquedo = pd.DataFrame(
    {
        'nome': ['teo', 'nah', 'mah'],
        'idade': [32, 35, 14],
        'uf': ['sp', 'pr', 'rj']

    }
)

filtro = brinquedo['idade'] >= 18
brinquedo[filtro]

# %%
df.shape
# %%
transacoes_m50 = df['QtdePontos'] >= 50
df[transacoes_m50]

# %%
transacoes_m50 = df['QtdePontos'] >= 50
df[transacoes_m50]

# %%
filtro = (df['QtdePontos'] >= 50) & (df['QtdePontos'] < 100)
df[filtro]

# %%
filtro = (df['QtdePontos'] == 1) | (df['QtdePontos'] == 100)
df[filtro]
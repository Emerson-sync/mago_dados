# %%
import pandas as pd
import numpy as np
# %%
df = pd.read_csv('../data/clientes.csv', sep=';')
cresc = df.sort_values('DtCriacao')
df.head(15)

# %%
# cria uma nova coluna, adicionando +100 pra cada linha da qtdePontos
df['pontos_100'] = df['qtdePontos'] + 100

# %%
# cria uma nova coluna com a soma de 
df['emailTwitch'] = df['flEmail'] + df['flTwitch']
df.sample(5)

# %%
df['emailTwitch_and'] = df['flEmail'] * df['flTwitch']
df.sample(5)

# %%
df['qtdePontos'].describe()
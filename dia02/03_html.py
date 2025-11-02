# %%
import pandas as pd

# %%
url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
# Adicionei um cabeçalho para simular um navegador e evitar o erro 403 (Forbidden)
headers = {'User-Agent': 'Mozilla/5.0'}
dfs = pd.read_html(url, storage_options=headers)
dfs

# %%
type(dfs)

# %%
len(dfs)

# %%
df_uf = dfs[1]
df_uf.to_csv("ufs.csv", sep=";", index=False)
df_uf.head()

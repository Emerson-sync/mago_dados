# %%
import pandas as pd

# %%
df = pd.read_csv('../dia02/ufs.csv', sep=';')
df.head()

# %%
df.sort_values('População (Censo 2022)')

# %%
df.shape
# %%
import pandas as pd

idades = [32, 38, 30, 30, 31, 35, 25, 
          29, 31, 37, 27, 23, 36, 33, 32]

# %%
series_idades = pd.Series(idades)
series_idades


# %% 
idades[0]

# %%
series_idades = series_idades.sort_values()
series_idades

# %%
series_idades.iloc[-1]

# %%
series_idades.iloc[:3]

# %%
indexs = ["Gabriel", "Juliana", "Mateus","Beatriz", "Rafael", 
         "Larissa", "Leonardo", "Amanda", "Bruno", "Carolina", 
         "Felipe", "Mariana", "Felipe", "Lucas", "Camila"
]

# %%
series_idades = pd.Series(idades, indexs)
series_idades

# %%
series_idades.iloc[0]

# %%
series_idades['Felipe']
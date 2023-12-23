import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ss13\population.csv')
df2 = df.head(20)
df3 = df2.sort_values(by='Population (2020)',ascending=False)
fig, ax = plt.subplots(figsize = (12, 5))
plt.bar(df3['Country (or dependency)'], df3['Population (2020)'], color='blue')
plt.xlabel('Country')
plt.ylabel('Population (2020)')
plt.title('Population of Countries in 2020')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.show()
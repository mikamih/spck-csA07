import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ss13\population.csv')
df.replace('N.A.', pd.NA, inplace=True)
df.dropna(inplace=True)

df2=df.head(20)
df2 = df2.sort_values(by='Med. Age')
fig, ax = plt.subplots(figsize = (12, 5))
plt.bar(df2['Country (or dependency)'], df2['Med. Age'], color='blue')
plt.xlabel('Country')
plt.ylabel('Med.Age')
plt.title('Med. Age in 2020')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.show()

print(df2)

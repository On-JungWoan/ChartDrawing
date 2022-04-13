import pandas as pd

url = 'c:/users/samsung/desktop/chart_chartdata.csv'
df = pd.read_csv(url)

temp = []
for i in range(len(df)):
    temp.append(df.date[i].split(' ')[0])
df['date_only'] = temp

print(df.groupby('date_only').mean())
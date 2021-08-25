import pandas as pd

df = pd.read_csv('articles.csv')

articals = df.sort_values('total_events', ascending=False)

output = articals[['title', 'text', 'url']].head(20).values.tolist()

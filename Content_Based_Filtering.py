import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


df = pd.read_csv('articles.csv')

count = CountVectorizer(stop_words='english')
count_metrix = count.fit_transform(df['soup'])

cosine_sim = cosine_similarity(count_metrix, count_metrix)

df = df.reset_index()
indices = pd.Series(df.index, index=df['title'])


def get_recommendation(title, cosine_sim=cosine_sim):
    index = indices[title]
    sim_scores = list(enumerate(cosine_sim[index]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1: 11]

    artical_indices = [i[0] for i in sim_scores]

    return df[['title', 'text', 'url']].iloc[artical_indices].values.tolist()

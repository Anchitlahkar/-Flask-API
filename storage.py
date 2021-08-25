import csv
with open('articles.csv', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)


allArticals = data[1:]

liked_articles = []
not_liked_articles = []
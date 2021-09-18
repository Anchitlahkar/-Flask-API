import csv
with open('articles.csv', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)

allArticals = []

for info in data:
    if info[14] == 'en':
        allArticals.append(info)

liked_articles = []
not_liked_articles = []

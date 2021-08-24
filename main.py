from flask import Flask, jsonify, request
import csv

with open('articles.csv',encoding='utf-8' ) as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)


allArticals = data[1:]

liked_articles = []
not_liked_articles = []


app = Flask(__name__)


@app.route('/')
def allData():
    artical = {
        'title': allArticals[0][12],
        'text': allArticals[0][13],
        'url': allArticals[0][11] or 'n/a',
    }
    return jsonify({
        'data': artical,
        'ststus': 'success'
    })


@app.route('/liked-articles', methods=['POST'])
def liked_articals():
    global allArticals

    artical = allArticals[0]
    liked_articles.append(artical)
    allArticals.pop(0)

    return jsonify({
        'status': 'success'
    })


@app.route('/not-liked-articles', methods=['POST'])
def not_liked_articals():
    global allArticals

    artical = allArticals[0]
    not_liked_articles.append(artical)
    allArticals.pop(0)

    return jsonify({
        'status': 'success'
    })


if __name__ == '__main__':
    app.run()

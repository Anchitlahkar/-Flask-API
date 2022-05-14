from storage import allArticals, liked_articles, not_liked_articles
from flask import Flask, jsonify, request
from Demographic_Filtering import output
from Content_Based_Filtering import get_recommendation

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


@app.route('/Demographic_Filtering')
def Demographic_Filtering():
    return jsonify({
        'data': output,
        'status': 'success'
    })


@app.route('/Content_Based_Filtering', methods=['POST'])
def Content_Based_Filtering():
    all_recommended = []
    for liked_article in liked_articles:
        output = get_recommendation(liked_article[15])
        print(liked_article[15])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,
                           _ in itertools.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        _d = {
            'title': recommended[0],
            'text': recommended[1],
            'url': recommended[2] or 'n/a',
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200


if __name__ == '__main__':
    app.run()

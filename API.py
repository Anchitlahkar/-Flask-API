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
    try:
        recommendation = liked_articles[0][15]
    
    except:
        recommendation = []
        pass

    return jsonify({
        'data': recommendation
    }), 200


if __name__ == '__main__':
    app.run()
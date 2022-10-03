from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


from pymongo import MongoClient

import certifi
ca = certifi.where()

client = MongoClient('mongodb+srv://eunshu12:<Mulberry1!>@cluster0.tmzwrco.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/step", methods=["POST"])
def movie_post():
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    doc={
        "star":star_receive,
        "comment":comment_receive
    }
    db.step2.insert_one(doc)

    return jsonify({'msg':'review 등록완료!'})

@app.route("/step/review", methods=["GET"])
def movie_get():
    review_list = list(db.step.find({}, {'_id': False}))
    return jsonify({'reviews':review_list})

if __name__ == '__main__':
app.run('0.0.0.0', port=5001, debug=True)
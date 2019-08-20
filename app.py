# import の実行
from flask import Flask
from flask import jsonify,request



# インスタンスの作成
app = Flask(__name__)
items = []

# URL, Methodと関数の紐づけ
@app.route('/',methods=['POST'])
def make_something():
    item = request.get_json()
    items.append(item)
    return jsonify(item)

# サーバの起動
app.run(host='0.0.0.0', port=80 , debug=True)

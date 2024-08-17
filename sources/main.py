import os
from flask import Flask, render_template, request
from output import KeyStroke
import time

app = Flask(__name__, static_folder=".")

# ルーティング

# login処理です
@app.route('/', methods=['GET', 'POST'])
def form():
    # ２回目以降データが送られてきた時の処理です
    if request.method == 'POST':
        ks = KeyStroke()
        ks.nextPage()
        time.sleep(1)
        ks.prevPage()

        # print("POSTされたIDは？" + str(request.form['id']))
        # print("POSTされたPASSWORDは？" + str(request.form['pwd']))
        return render_template('form.html')
    # １回目のデータが何も送られてこなかった時の処理です。
    if request.method == 'GET':
        return render_template('form.html')

if __name__ == "__main__":
    app.run(port=1145)
    # app.run(port=1145, debug=False, host="0.0.0.0")
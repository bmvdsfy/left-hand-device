import time

from flask import Flask, render_template, request, url_for
from option_parser import get_option
from output import KeyStroke

app = Flask(__name__)

# ルーティング

@app.route('/', methods=['GET', 'POST'])
def form():
    # ２回目以降データが送られてきた時の処理です
    if request.method == 'POST':
        # ks = KeyStroke()
        # ks.nextPage()
        # time.sleep(1)
        # ks.prevPage()

        return render_template('form.html')
    
    if request.method == 'GET':
        return render_template('form.html')


if __name__ == "__main__":
    args = get_option()

    if args.host:
        app.run(port=1145, debug=False, host="0.0.0.0")
    else:
        app.run(port=1145)
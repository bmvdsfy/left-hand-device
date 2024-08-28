# import time


from config.config import shortcuts
from config.general import general_config
from flask import Flask, redirect, render_template, request, url_for
from option import get_option
from output import key_press

app = Flask(__name__)




# ルーティング
@app.route('/', methods=['GET', 'POST'])
def form():
    # ２回目以降データが送られてきた時の処理です
    if request.method == 'POST':
        print(request.form.get("shortcut"))
        requested_shortcut = request.form.get("shortcut")

        for shortcut in shortcuts:
            if shortcut["name"] == requested_shortcut:
                key_press(shortcut)
                break
        
        return redirect(url_for("form"))
    
    if request.method == 'GET':
        return render_template('form.html', shortcuts=shortcuts, column=general_config["column"], row=general_config["row"])


if __name__ == "__main__":
    args = get_option()

    if args.host:
        app.run(port=2109, debug=True, host="0.0.0.0")
    else:
        app.run(port=2109)
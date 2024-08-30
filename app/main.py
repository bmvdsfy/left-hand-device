# import time


from config.config import shortcuts
from config.general import general_config
from flask import Flask, redirect, render_template, request, url_for
from option import get_option
from output import proceed_shortcut
from exept import exept_out_of_range

app = Flask(__name__)




# ルーティング
@app.route('/', methods=['GET', 'POST'])
def form():
    # ２回目以降データが送られてきた時の処理
    if request.method == 'POST':
        #リクエストされたボタンに対応するショートカットを実行
        print(r'requested "' + request.form.get("shortcut") + r'"')
        requested_shortcut = request.form.get("shortcut")

        for shortcut in shortcuts:
            if shortcut["name"] == requested_shortcut:
                proceed_shortcut(shortcut)
                break
        
        #リロード対策のリダイレクト
        return redirect(url_for("form"))
    
    if request.method == 'GET':
        exept_out_of_range(shortcuts, general_config)
        template = render_template(general_config["style"], shortcuts=shortcuts, column=general_config["column"], row=general_config["row"])
        # print(template)
        return template


if __name__ == "__main__":
    args = get_option()

    if args.host:
        app.run(port=2109, debug=True, host="0.0.0.0")
    else:
        app.run(port=2109)
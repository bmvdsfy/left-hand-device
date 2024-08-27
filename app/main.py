# import time
from keytype import Shortcut


from flask import Flask, render_template, request
from option import get_option

from output import key_press

app = Flask(__name__)

shortcuts: list[Shortcut] = [
    {
        "id": 1,
        "name": "undo",
        "key": ["command", "z"]
    },
    {
        "id": 2,
        "name": "redo",
        "key": ["command", "shiftleft", "z"]
    },
    {
        "id": 3,
        "name": "none",
        "key": []
    },
    {
        "id": 4,
        "name": "none",
        "key": []
    },
    {
        "id": 5,
        "name": "none",
        "key": []
    },
    {
        "id": 6,
        "name": "none",
        "key": []
    },
    {
        "id": 7,
        "name": "検索",
        "key": ["command", "l", ]
    },
    {
        "id": 8,
        "name": "previousPage",
        "key": ["command", "option", "left", ]
    },
    {
        "id": 9,
        "name": "nextPage",
        "key": ["command", "option", "right", ]
    }
]





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
    
        return render_template('form.html', shortcut_lists=shortcuts, column=3, row=3)
    
    if request.method == 'GET':
        return render_template('form.html', shortcut_lists=shortcuts, column=3, row=3)


if __name__ == "__main__":
    args = get_option()

    if args.host:
        app.run(port=2109, debug=True, host="0.0.0.0")
    else:
        app.run(port=2109)
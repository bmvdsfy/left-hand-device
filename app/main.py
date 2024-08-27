# import time
from typing import TypedDict

from flask import Flask, render_template, request
from option import get_option

# from output import KeyStroke

app = Flask(__name__)

class Shortcuts(TypedDict):
    id: int
    name: str
    key: list[str]

shortcuts: Shortcuts = [
    {
        "id": 1,
        "name": "undo",
        "key": ["ctrl", "z"]
    },
    {
        "id": 2,
        "name": "redo",
        "key": ["ctrl", "shift", ]
    },
    {
        "id": 3,
        "name": "redo",
        "key": ["ctrl", "shift", ]
    },
    {
        "id": 4,
        "name": "redo",
        "key": ["ctrl", "shift", ]
    },
    {
        "id": 5,
        "name": "redo",
        "key": ["ctrl", "shift", ]
    },
    {
        "id": 6,
        "name": "redo",
        "key": ["ctrl", "shift", ]
    },
    {
        "id": 7,
        "name": "redo",
        "key": ["ctrl", "shift", ]
    },
    {
        "id": 8,
        "name": "redo",
        "key": ["ctrl", "shift", ]
    },
    {
        "id": 9,
        "name": "redo",
        "key": ["ctrl", "shift", ]
    }
]





# ルーティング
@app.route('/', methods=['GET', 'POST'])
def form():
    # ２回目以降データが送られてきた時の処理です
    if request.method == 'POST':
        print(request.form.get("shortcut"))
    
        return render_template('form.html', shortcut_lists=shortcuts, column=3, row=3)
    
    if request.method == 'GET':
        return render_template('form.html')


if __name__ == "__main__":
    args = get_option()

    if args.host:
        app.run(port=2109, debug=False, host="0.0.0.0")
    else:
        app.run(port=2109)
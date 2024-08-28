from keytype import Shortcut
shortcuts: list[Shortcut] = [
    {
        "id": 1,
        "name": "undo",
        "key": ["command", "z"],
        "position": {
            "row": 1,
            "column": 1
        }
    },
    {
        "id": 2,
        "name": "redo",
        "key": ["command", "shiftleft", "z"],
        "position": {
            "row": 1,
            "column": 2
        }
    },
    {
        "id": 3,
        "name": "none",
        "key": [],
        "position": {
            "row": 1,
            "column": 3
        }
    },
    {
        "id": 4,
        "name": "none",
        "key": [],
        "position": {
            "row": 2,
            "column": 1
        }
    },
    {
        "id": 5,
        "name": "none",
        "key": [],
        "position": {
            "row": 2,
            "column": 2
        }
    },
    {
        "id": 6,
        "name": "none",
        "key": [],
        "position": {
            "row": 2,
            "column": 3
        }
    },
    {
        "id": 7,
        "name": "検索",
        "key": ["command", "l", ],
        "position": {
            "row": 3,
            "column": 1
        }
    },
    {
        "id": 8,
        "name": "previousTab",
        "key": ["command", "option", "left", ],
        "position": {
            "row": 3,
            "column": 2
        }
    },
    {
        "id": 9,
        "name": "nextTab",
        "key": ["command", "option", "right", ],
        "position": {
            "row": 3,
            "column": 3
        }
    }
]
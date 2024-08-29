from typing import TypedDict

# class Keystroke(TypedDict):
# ショートカットに関する設定を置く型
class Position(TypedDict):
    row: int
    column: int

class ShortcutOptionalType(TypedDict, total=False):
    id: int
    description: str
    position: Position

class Shortcut(ShortcutOptionalType):
    name: str
    key: list[str]




class GeneralConfig(Position):
    pass

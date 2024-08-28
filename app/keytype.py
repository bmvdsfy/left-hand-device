from typing import TypedDict

# class Keystroke(TypedDict):

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

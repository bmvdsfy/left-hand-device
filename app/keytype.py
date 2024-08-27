from typing import TypedDict

# class Keystroke(TypedDict):

class ShortcutOptionalType(TypedDict):
    id: int
    description: str

class Shortcut(ShortcutOptionalType):
    name: str
    key: list[str]

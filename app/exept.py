from keytype import Shortcut, GeneralConfig

def exept_out_of_range(shortcuts: list[Shortcut], general_config: GeneralConfig):
    for shortcut in shortcuts:
        if shortcut["position"]["row"] > general_config["row"] or shortcut["position"]["column"] > general_config["column"]:
            shortcuts.remove(shortcut)
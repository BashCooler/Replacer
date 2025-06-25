import time
from os import path, startfile
import yaml
import keyboard as kb
import pystray as tray
import threading
import functools
from PIL import Image

BASE_DIR = path.dirname(path.abspath(__file__))
RULE_LOC = path.join(BASE_DIR, "src", "rules.yaml")


def replace(trigger, replacement):
    for _ in trigger + ' ':
        kb.send('backspace')
    time.sleep(0.01)
    kb.write(replacement + ' ')


def set_keyboard_listener():
    # Load rules from YAML
    with open(RULE_LOC, "r", encoding="utf-8") as file:
        rules = yaml.safe_load(file)
    # Add hotkeys
    for key, val in rules.items():
        callback = functools.partial(replace, key, val)
        kb.add_word_listener(key, callback)
    # Await hotkeys
    kb.wait()


def set_tray_icon():
    icon = tray.Icon(
        "Symbol Replacer",
        Image.open(path.join(BASE_DIR, "src", "replace.png")),
        "Symbol Replacer",
        tray.Menu(
            tray.Menu.SEPARATOR,  # does nothing, moves PyCharm hint
            tray.MenuItem("Edit hotkeys", lambda: startfile(RULE_LOC)),
            tray.MenuItem("Exit", tray.Icon.stop)
        )
    )
    icon.run()


def main():
    threading.Thread(target=set_keyboard_listener, daemon=True).start()
    set_tray_icon()


if __name__ == "__main__":
    main()

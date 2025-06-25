# What is it?

**Replacer** allows you to replace specific keyboard input in real time.

# Quick start

Follow these few steps after building or downloading this application to set everything up.

1. Launch replacer.exe
2. Right click on icon in system tray, then press `Edit hotkeys`
3. Specify replaces in opened YAML file like this
```YAML
trigger_word_1 : replace_word_1
trigger_word_2 : replace_word_2
```
4. Close application by pressing `Exit` in system tray menu
5. Start again to apply changes

Now you can type (for this example) `trigger_word_1` and after pressing `Space` it will be automatically replaced to `replace_word_1` (as specified in YAML earlier).

# How to build

In the `Replacer` directory (same one where `replacer.py` located), execute:

`pyinstaller -y -w --add-data "src/replace.png:." --add-data "src/rules.yaml:." --add-data "src/replace.ico:." --icon=replace.ico replacer.py`

The results are available in `dist` folder.
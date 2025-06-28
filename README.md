## What is it?

**Replacer** allows you to replace specific keyboard input in real time.

## Quick start

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

## Configuration

You can configure these parameters in `src/config.yaml`:

- **Delay** – if you're having issues replacing the first word in string, try a higher `Delay` value
- **Timeout** – maximum number of seconds between typed characters before the current word is discarded

## How to build

In the `Replacer` directory (same one where `replacer.py` located), execute:

```
pyinstaller -y -w --add-data "src/replace.png:src" --add-data "src/rules.yaml:src" --add-data "src/replace.ico:src" --add-data "src/config.yaml:src"  --icon=src/replace.ico --hidden-import=win32timezone --hidden-import=plyer.platforms.win.notification replacer.py
```

The results will be available in `dist` folder.

___

## Credits

Icon : https://tabler.io/icons

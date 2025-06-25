# What is it?

**Replacer** allows you to replace

# How to build

In the `Replacer` directory (same one where `replacer.py` located), execute:

`pyinstaller -y -w --add-data "src/replace.png:." --add-data "src/rules.yaml:." --add-data "src/replace.ico:." --icon=replace.ico replacer.py`

The results are available in `dist` folder.
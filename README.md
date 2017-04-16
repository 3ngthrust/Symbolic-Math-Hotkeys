# symbolic-math-hotkeys
Short script to make easily rememberable keyboard shortcuts (hotkeys) for writing greek symbols in unicode and LaTeX available.

Currently only Linux supported.

Usage
-----
1. Start the script:
```python
python3 symbolic_math_hotkeys.py
```
If used often, it is convinient to start the script on startup.

2. Press "AltGr" and afterwards a key of your choice to write the corresponding greek symbol.
```
  a -> α
  b -> β
  p -> π
  D -> Δ
  ...
```
To switch to LaTeX output press "AltGr", "Shift" and "l" one after another.
```
  a -> \alpha
  b -> \beta
  p -> \pi
  D -> \Delta
  ...
```
To see all possible shortcuts view the dicts in the code.

By default the script runs indefinitely.
To stop the script press the combination "Ctrl+C" in the terminal where the script runs.

Uses the keyboard module v0.9.13 form https://github.com/boppreh/keyboard.

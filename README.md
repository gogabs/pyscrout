# Pyscrout

Pyscrout sends text to be **spoken **and displayed in **braille **by screen readers.

## Motivation

The usual way to use screen readers to output some text in this way, is to use [accessible_output2](https://pypi.org/project/accessible-output2/), however the library is not well maintained and it's not compatible with Python 3.10 or later.

However, Pyscrout isn't a perfect replacement yet. Currently, it only supports NVDA on Windows, with no timeline to add support for other screen readers or operating systems.

## Installation

Install the library using **pip** :

```shell
pip install pyscrout@git+https://github.com/gogabs/pyscrout
```

Pyscrout comes with the controller DLL already included downloaded from https://download.nvaccess.org/releases/. It's a 64-bit DLL, so if you need the 32-bit one, you may need to swap the files.

## Usage

First, import the library:

```python
from pyscrout import nvda
```

You can use `nvda.is_running` to check if NVDA is running or not:

```python
if nvda.is_running():  # Returns a bool
    print("NVDA is up and running!)
else:
    print("Nope, not running)
```

You can use `nvda.speak`, `nvda.braille` or `nvda.output` to make NVDA **speak**, **braille** or **speak AND braille** a string:

```python
# Speech only
nvda.speak("Hello, World!")

# Same as above, but interrupts current speech before speaking
nvda.speak("Hello, World!", interrupt=True)

# Braille only
nvda.braille("Hello, World!")

# Both speech and braille
nvda.output("Hello, World!")

# Also interrupts current speech
nvda.output("Hello, World!", interrupt=True)
```

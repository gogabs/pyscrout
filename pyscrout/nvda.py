import ctypes
from pathlib import Path
import sys

lib_path = Path(__file__).parent / "lib/nvdaControllerClient.dll"


nvda_lib = None

if sys.platform == "win32":
    nvda_lib = ctypes.windll.LoadLibrary(str(lib_path))


def is_available() -> bool:
    """
    Checks if NVDA is available in this platform

    :return: True if NVDA is available and running, False otherwise
    :rtype: bool
    """

    if not nvda_lib:
        return False

    res: int = nvda_lib.nvdaController_testIfRunning()
    return res == 0


def speak(text: str, *, interrupt: bool = False):
    """Sends the given text to NVDA to be spoken

    Arguments:
    text: str -- The text to be spoken
    interrupt: bool -- If True, makes NVDA interrupt any text it's currently speaking before speaking the given text (default False)
    """

    if not is_available():
        return

    if interrupt:
        nvda_lib.nvdaController_cancelSpeech()

    nvda_lib.nvdaController_speakText(text)


def braille(text: str):
    """Sends the given text to NVDA to be displayed in braille

    Arguments:
    text: str -- The text to be displayed in braille
    """

    if not is_available():
        return

    nvda_lib.nvdaController_brailleMessage(text)


def output(text: str, interrupt: bool = False):
    """Sends the given text to NVDA to be spoken and displayed in braille

    Arguments:
    text: str -- The text to be sent to NVDA
    interrupt: bool -- If True, makes NVDA interrupt any text it's currently speaking before speaking the given text (default False)
    """

    speak(text, interrupt=interrupt)
    braille(text)

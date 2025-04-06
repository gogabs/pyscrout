import ctypes
from pathlib import Path

lib_path = Path(__file__).parent / "lib/nvdaControllerClient.dll"

nvda_lib = ctypes.windll.LoadLibrary(str(lib_path))


def speak(text: str, *, interrupt: bool = False):
    """Sends the given text to NVDA to be spoken

    Arguments:
    text: str -- The text to be spoken
    interrupt: bool -- If True, makes NVDA interrupt any text it's currently speaking before speaking the given text (default False)
    """

    if interrupt:
        nvda_lib.nvdaController_cancelSpeech()

    nvda_lib.nvdaController_speakText(text)


def braille(text: str):
    """Sends the given text to NVDA to be displayed in braille

    Arguments:
    text: str -- The text to be displayed in braille
    """

    nvda_lib.nvdaController_brailleMessage(text)


def output(text: str, interrupt: bool = False):
    """Sends the given text to NVDA to be spoken and displayed in braille

    Arguments:
    text: str -- The text to be sent to NVDA
    interrupt: bool -- If True, makes NVDA interrupt any text it's currently speaking before speaking the given text (default False)
    """

    speak(text, interrupt=interrupt)
    braille(text)


def is_running() -> bool:
    """Checks if NVDA is running

    Returns
    bool -- True if NVDA is running, False otherwise
    """

    res: int = nvda_lib.nvdaController_testIfRunning()
    return res == 0

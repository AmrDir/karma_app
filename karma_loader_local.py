
import os

BASE_PATH = "/content/drive/MyDrive/KARMA_CHAT/Karma_House/Core_Memory"

def load_static_memory():
    file_path = os.path.join(BASE_PATH, "static_memory.txt")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

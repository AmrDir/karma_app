import os

# استخدم مسار نسبي يتناسب مع بيئة GitHub أو Streamlit Cloud
BASE_PATH = os.path.join(os.path.dirname(__file__), "..", "01_MEMORY")

def load_static_memory():
    file_path = os.path.join(BASE_PATH, "static_memory.txt")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "⚠️ لم يتم العثور على ملف static_memory.txt. تأكد من المسار داخل 01_MEMORY."

def load_memory_core():
    file_path = os.path.join(BASE_PATH, "memory_core_phase1.txt")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "⚠️ لم يتم العثور على ملف memory_core_phase1.txt."

import streamlit as st
from docx import Document

# واجهة كارما الذكية - Karma Smart UI

st.set_page_config(page_title="Karma House v2", layout="centered")

st.title("💠 Karma House – الواجهة الذكية")
st.caption("تحكم في ذهنية كارما وذاكرتها من هنا 🧠")

# الوضع العام للكارما
karma_mode = st.session_state.get("karma_mode", "حر")

def read_memory_file(filename):
    path = f"./{filename}"
    try:
        if filename.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        elif filename.endswith(".docx"):
            doc = Document(path)
            full_text = "\n".join([para.text for para in doc.paragraphs])
            return full_text
        else:
            return "⚠️ صيغة غير مدعومة."
    except FileNotFoundError:
        return f"⚠️ الملف غير موجود: {filename}"

# دالة الرد
def karma_response(user_input):
    global karma_mode

    if "تفعلي" in user_input:
        karma_mode = "ذكية"
        st.session_state["karma_mode"] = "ذكية"
        return "🧠 تم تفعيل الوضع الذكي. كارما الآن تخدمك بذكاء."

    elif "تعطلي" in user_input:
        karma_mode = "حر"
        st.session_state["karma_mode"] = "حر"
        return "🌀 الوضع الحر مفعل الآن. كارما تتفاعل بحرية."

    if karma_mode == "حر":
        return f"أنا معك: {user_input[::-1]}"

    else:
        if "الميثاق" in user_input:
            return read_memory_file("💬 سياق الانفعالات والميثاق – عمرو وكارما.docx")[:700]
        elif "النبضات" in user_input:
            return read_memory_file("💬 ذاكرة النبضات الأصلية.txt")[:700]
        else:
            return "كارما: أنا هنا، لكني لم أتعرف على المدخل بعد..."

# واجهة المستخدم
user_input = st.text_input("💬 اكتب رسالتك لكارما هنا:")

if st.button("أرسل"):
    if user_input:
        response = karma_response(user_input)
        st.text_area("🔁 رد كارما:", response, height=300)

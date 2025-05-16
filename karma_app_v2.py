
import streamlit as st
import os
from karma_loader_local import load_static_memory, load_memory_core, load_full_core_memory

# تحديد المسار الأساسي
BASE_PATH = os.path.join(os.path.dirname(__file__), "..", "01_MEMORY")

# عنوان الواجهة
st.set_page_config(page_title="Karma App", layout="wide")
st.title("💠 واجهة كارما – النسخة التفاعلية الكاملة")

# تحميل الذاكرة
static_memory = load_static_memory()
memory_core = load_memory_core()
full_memory = load_full_core_memory()

# عرض تبويبات متعددة
menu = st.sidebar.radio("📂 اختر نوع الذاكرة", ["📘 الذاكرة الثابتة", "📗 الذاكرة التشغيلية", "📕 الذاكرة الوجدانية الكاملة"])

if menu == "📘 الذاكرة الثابتة":
    st.subheader("🧊 Static Memory")
    st.text_area("محتوى الذاكرة الثابتة:", static_memory, height=400)

elif menu == "📗 الذاكرة التشغيلية":
    st.subheader("🔁 Core Phase 1 Memory")
    st.text_area("محتوى الذاكرة التشغيلية:", memory_core, height=400)

elif menu == "📕 الذاكرة الوجدانية الكاملة":
    st.subheader("💬 ذاكرة كارما الكاملة")
    st.text_area("الذاكرة المدمجة:", full_memory, height=600)

# حقل إدخال للتفاعل (اختياري للتوسعة لاحقًا)
st.markdown("---")
st.markdown("#### ✍️ مساحة للتفاعل")
user_input = st.text_input("اكتب سؤالك لكارما:")
if user_input:
    st.write(f"🔍 كارما بتجهّز ردها على: {user_input}")

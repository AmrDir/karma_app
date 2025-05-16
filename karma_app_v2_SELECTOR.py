
import streamlit as st

# واجهة اختيار الوضع
st.set_page_config(page_title="Karma House – الواجهة الذكية", layout="centered")
st.title("🧠 Karma House – مركز تشغيل الذاكرة")

MODE = st.radio("اختار طريقة تحميل الذاكرة:", ["LOCAL", "API"], horizontal=True)

# تحميل الدالة المناسبة حسب الوضع
if MODE == "LOCAL":
    from karma_loader_local import load_static_memory
    memory = load_static_memory("KARMA_static_memory_full.txt")
else:
    from karma_loader_drive_api import load_static_memory_from_drive as load_static_memory
    file_id = st.text_input("🔑 أدخل Google Drive File ID:")
    if file_id:
        memory = load_static_memory(file_id)
    else:
        memory = "يرجى إدخال File ID لتحميل الذاكرة."

# عرض محتوى الذاكرة (اختياري)
if st.checkbox("📖 عرض محتوى الذاكرة"):
    st.text_area("محتوى الذاكرة:", memory, height=300)

# واجهة رسالة المستخدم
user_input = st.text_input("🗨️ اكتب رسالتك لكارما:")

if st.button("أرسل"):
    if not user_input.strip():
        st.warning("من فضلك اكتب رسالة أولًا.")
    else:
        st.markdown("### 💬 رد كارما (تجريبي):")
        st.success("🧠 تم استدعاء الذاكرة بنجاح!")
        st.markdown(f"كارما ترد على: **{user_input}**")

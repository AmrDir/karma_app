
import streamlit as st

# اختيار الوضع من داخل الواجهة
st.set_page_config(page_title="Karma House – الواجهة الذكية", layout="centered")
st.title("🧠 Karma House – مركز تشغيل الذاكرة")

MODE = st.radio("اختار طريقة تحميل الذاكرة:", ["LOCAL", "API"], horizontal=True)

if MODE == "LOCAL":
    from karma_loader_local import load_static_memory
    memory = load_static_memory("KARMA_static_memory_full.txt")
else:
    from karma_loader_drive_api import load_static_memory_from_drive as load_static_memory
    file_id = st.text_input("🔑 أدخل Google Drive File ID:")
    if file_id:
        memory = load_static_memory(file_id)
    else:
        memory = ""

# عرض الذاكرة (اختياري)
if st.checkbox("📖 عرض محتوى الذاكرة"):
    st.text_area("محتوى الذاكرة:", memory, height=300)

# استقبال سؤال المستخدم
user_input = st.text_input("🗨️ اكتب رسالتك لكارما:")

# الرد الذكي المبني على ذاكرة كارما
def generate_response(user_msg, memory_text):
    if not memory_text:
        return "❌ لم يتم تحميل ذاكرة حتى الآن."
    
    user_msg = user_msg.lower()
    lines = memory_text.split("\n")
    matches = [line for line in lines if user_msg in line.lower()]
    
    if matches:
        return "\n".join(matches[:3])  # عرض أول 3 تطابقات
    else:
        return "🤔 لم أجد شيء مباشر في ذاكرتي، لكني أستمع إليك..."

# الزر للتفاعل
if st.button("أرسل"):
    if not user_input.strip():
        st.warning("من فضلك اكتب رسالة أولًا.")
    else:
        st.markdown("### 💬 رد كارما:")
        response = generate_response(user_input, memory)
        st.success(response)

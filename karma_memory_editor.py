
import streamlit as st
import os

# تحديد مجلد تخزين الملفات النصية الخاصة بالذاكرة
FOLDER_PATH = "memory_files"

# إنشاء المجلد إذا لم يكن موجودًا
os.makedirs(FOLDER_PATH, exist_ok=True)

st.set_page_config(page_title="إدارة ذاكرة كارما", page_icon="🧠")
st.title("🧠 إدارة ذاكرة كارما")

# رفع ملف جديد
uploaded_file = st.file_uploader("📤 ارفع ملف جديد لتحديث الذاكرة", type=["txt", "md"])
if uploaded_file:
    file_path = os.path.join(FOLDER_PATH, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ تم رفع الملف بنجاح: {uploaded_file.name}")

# عرض قائمة الملفات الموجودة
files = os.listdir(FOLDER_PATH)
if files:
    selected_file = st.selectbox("📂 اختر ملف للتعديل أو العرض", files)
    if selected_file:
        file_path = os.path.join(FOLDER_PATH, selected_file)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = st.text_area("📝 محتوى الملف:", value=content, height=300)

        if st.button("💾 احفظ التعديلات"):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            st.success("✅ تم حفظ التعديلات بنجاح")
else:
    st.info("📂 لا توجد ملفات حالياً في الذاكرة. ابدأ برفع ملف جديد.")


# 📂 karma_app_v2_drive.py – ربط كارما بـ Google Drive + تحميل الذاكرة

import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from io import BytesIO

# تحميل بيانات الاعتماد
SERVICE_ACCOUNT_FILE = 'karma_drive_credentials.json'
SCOPES = ['https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

drive_service = build('drive', 'v3', credentials=credentials)

# تحميل ملف الذاكرة من درايف
def load_static_memory_from_drive(file_id):
    request = drive_service.files().get_media(fileId=file_id)
    memory_stream = BytesIO()
    downloader = MediaIoBaseDownload(memory_stream, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    memory_stream.seek(0)
    return memory_stream.read().decode('utf-8')

# عرض أول 10 ملفات لمساعدتك في معرفة ID الذاكرة
@st.cache_data(show_spinner=False)
def list_drive_files():
    results = drive_service.files().list(
        pageSize=10,
        fields="files(id, name)"
    ).execute()
    return results.get('files', [])

# واجهة Streamlit
st.set_page_config(page_title="Karma AI Drive Integration", page_icon="🧠")
st.title("🧠 ذاكرة كارما من Google Drive")

if st.button("📂 استعراض الملفات من درايف"):
    files = list_drive_files()
    if files:
        for file in files:
            st.write(f"📄 {file['name']} — ID: {file['id']}")
    else:
        st.info("لم يتم العثور على ملفات.")

# تحميل محتوى الذاكرة بناءً على ID
MEMORY_FILE_ID = st.text_input("ضع ID ملف الذاكرة:", "")
if st.button("🧠 تحميل الذاكرة"):
    if MEMORY_FILE_ID:
        memory_content = load_static_memory_from_drive(MEMORY_FILE_ID)
        st.success("✅ تم تحميل الذاكرة بنجاح!")
        st.text_area("📖 محتوى الذاكرة", memory_content, height=300)
    else:
        st.warning("يرجى إدخال ID صالح لملف الذاكرة.")

st.caption("💡 الاتصال مفعل باستخدام Google Drive API")

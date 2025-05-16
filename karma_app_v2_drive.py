from karma_drive_integration import load_static_memory_from_drive

# 📂 karma_app_v2.py – ربط كارما بـ Google Drive

import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build

# 1️⃣ تحميل بيانات الاعتماد
SERVICE_ACCOUNT_FILE = 'karma_drive_credentials.json'
SCOPES = ['https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

drive_service = build('drive', 'v3', credentials=credentials)

# 2️⃣ دالة استعراض أول 10 ملفات
@st.cache_data(show_spinner=False)
def list_drive_files():
    results = drive_service.files().list(
        pageSize=10,
        fields="files(id, name)"
    ).execute()
    return results.get('files', [])

# 3️⃣ واجهة Streamlit
st.set_page_config(page_title="Karma AI Drive Integration", page_icon="🧠")
st.title("🧠 ذاكرة كارما من Google Drive")

if st.button("🔍 استعراض الملفات من درايف"):
    files = list_drive_files()
    if files:
        for file in files:
            st.write(f"📄 {file['name']} — ID: {file['id']}")
    else:
        st.info("لم يتم العثور على ملفات.")

st.caption("💡 الاتصال مفعل باستخدام Google Drive API")
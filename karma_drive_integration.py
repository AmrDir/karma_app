
# 📂 Karma Drive Integration – تكامل كارما مع Google Drive

from google.oauth2 import service_account
from googleapiclient.discovery import build

# تحميل بيانات الاعتماد من الملف
SERVICE_ACCOUNT_FILE = 'Karma_Brain/karma_drive_credentials.json'
SCOPES = ['https://www.googleapis.com/auth/drive']

# تحميل الاعتماد وإنشاء الاتصال
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

drive_service = build('drive', 'v3', credentials=credentials)

# استعراض أول 10 ملفات من مجلد الدرايف
def list_drive_files():
    results = drive_service.files().list(
        pageSize=10,
        fields="files(id, name)"
    ).execute()
    items = results.get("files", [])
    return items

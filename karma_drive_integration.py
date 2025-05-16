
# 📂 Karma Drive Integration – تكامل كارما مع Google Drive

from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = 'Karma_Brain/karma_drive_credentials.json'
SCOPES = ['https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

drive_service = build('drive', 'v3', credentials=credentials)

def list_drive_files():
    results = drive_service.files().list(
        pageSize=10,
        fields="files(id, name)"
    ).execute()
    items = results.get("files", [])
    return items

def load_static_memory_from_drive(file_name='static_memory.txt', download_path='downloaded_static_memory.txt'):
    # البحث عن الملف بالاسم
    query = f"name = '{file_name}' and trashed=false"
    results = drive_service.files().list(q=query, fields="files(id, name)").execute()
    items = results.get("files", [])
    
    if not items:
        raise FileNotFoundError(f"❌ لم يتم العثور على الملف: {file_name}")

    file_id = items[0]['id']

    from googleapiclient.http import MediaIoBaseDownload
    import io

    request = drive_service.files().get_media(fileId=file_id)
    fh = io.FileIO(download_path, 'wb')
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while not done:
        status, done = downloader.next_chunk()

    with open(download_path, 'r', encoding='utf-8') as f:
        return f.read()

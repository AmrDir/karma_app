
# 📂 test_drive_loader.py – اختبار تحميل الذاكرة من درايف

from KARMA_FINAL_KarmaDriveLoader import load_memory_from_drive

def main():
    print("⏳ جاري اختبار تحميل الذاكرة من Google Drive...")
    memory = load_memory_from_drive()

    if memory:
        print("✅ تم تحميل الذاكرة بنجاح:")
        print(memory[:500])  # عرض أول 500 حرف كمثال
    else:
        print("⚠️ لم يتم تحميل أي بيانات. تحقق من الاتصال أو اسم الملف.")

if __name__ == "__main__":
    main()

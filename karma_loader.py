
# karma_loader.py
MODE = "LOCAL"  # اختر بين 'LOCAL' أو 'API'

if MODE == "LOCAL":
    from karma_loader_local import load_static_memory
elif MODE == "API":
    from karma_loader_drive_api import load_static_memory_from_drive as load_static_memory
else:
    raise ValueError("❌ الوضع غير معروف: اختر 'LOCAL' أو 'API'")

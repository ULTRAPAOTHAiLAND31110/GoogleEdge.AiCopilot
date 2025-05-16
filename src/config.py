import os

# อ่าน API Key จาก environment variable
API_KEY = os.getenv('GOOGLE_EDGE_API_KEY', 'YOUR_DEFAULT_API_KEY')

# ตัวอย่างการใช้งาน API_KEY ในฟังก์ชัน

def get_google_edge_api_key():
    """
    คืนค่า API Key ที่อ่านได้จาก environment variable
    """
    return API_KEY

def aotorobot_mode_enabled():
    """
    ฟังก์ชันสำหรับตรวจสอบหรือเปิดโหมด AOTOROBOT เพื่อความสะดวกในการใช้งานระบบ
    สามารถนำไปใช้เป็น flag หรือ utility function ในส่วนอื่น ๆ ของโปรเจกต์
    """
    return True  # กำหนดค่า True เพื่อเปิดโหมดอัตโนมัติ

# ตัวอย่างการใช้งานร่วมกับ API Key

def get_aotorobot_api_key():
    """
    คืนค่า API Key เฉพาะเมื่อโหมด AOTOROBOT เปิดใช้งาน
    """
    if aotorobot_mode_enabled():
        return get_google_edge_api_key()
    return None

# สามารถเพิ่ม config หรือ utility อื่น ๆ ที่เกี่ยวข้องกับ API Key ได้ที่นี่

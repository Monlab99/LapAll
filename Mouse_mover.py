import pyautogui
import time
import datetime

# --- การตั้งค่า ---
INTERVAL_MINUTES = 20  # ตั้งค่าช่วงเวลา (นาที) ที่ต้องการให้เมาส์ขยับ
MOVE_PIXELS = 10       # ระยะพิกเซลที่จะขยับเมาส์ (เล็กน้อย)
# -----------------

# คำนวณวินาที
INTERVAL_SECONDS = INTERVAL_MINUTES * 60

print(">>> โปรแกรมขยับเมาส์อัตโนมัติ เริ่มทำงานแล้ว <<<")
print(f"จะทำการขยับเมาส์ทุกๆ {INTERVAL_MINUTES} นาที")
print("กด Ctrl + C เพื่อหยุดการทำงานของโปรแกรม")
print("-" * 40)

try:
    while True:
        # พิมพ์สถานะปัจจุบันและเวลารอก่อนเริ่มนับถอยหลัง
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{current_time}] สถานะ: ปกติ, รออีก {INTERVAL_MINUTES} นาที...")

        # รอตามเวลาที่กำหนด
        time.sleep(INTERVAL_SECONDS)

        # ขยับเมาส์เล็กน้อยเพื่อ "ปลุก" ระบบ
        print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] >>> กำลังขยับเมาส์...")

        # ขยับไปทางขวาเล็กน้อย แล้วขยับกลับที่เดิม
        # เพื่อไม่ให้ตำแหน่งเมาส์เปลี่ยนไปจากเดิมมาก
        pyautogui.moveRel(MOVE_PIXELS, 0, duration=0.2)  # ขยับไปทางขวา
        time.sleep(0.1)
        pyautogui.moveRel(-MOVE_PIXELS, 0, duration=0.2) # ขยับกลับมาทางซ้าย

        print("ขยับเมาส์เรียบร้อย! กลับสู่สถานะรอ...")
        print("-" * 40)

except KeyboardInterrupt:
    print("\n>>> หยุดการทำงานของโปรแกรมตามคำสั่งผู้ใช้ <<<")
except Exception as e:
    print(f"\nเกิดข้อผิดพลาด: {e}")
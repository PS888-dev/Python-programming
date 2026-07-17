#Module แยกไฟล์ จาก Main เพื่อแยกหมวดหมู่
#อันนี้คือmain โปรแกรมหลัก มีหน้าที่ run
#วิธีเรียกเข้า กรณีใช้ import ต้องระบุชื่อโมดูลกำกับ แต่ใช้ from import ไม่ต้องระบุชื่อโมดูลกำกับ ตั้งชื่อใหม่ได้โดยการใช้คำสั่ง as ทั้งสองแบบ ใช้ชื่อใหม่ระบุใช้งาน เอามาทุกฟังก์ชั่น ใช้ *
# import moduleC as mycal
# import moduleB as db
# #ใช้ import ต้องเรียกคำส่งตามพร้อมฟังก์ชั่นต่อ
# print(mycal.add(10,20)) 
# print(mycal.subtract(100,5))
# print(mycal.power(2,3))

# db.insert()
# print(db.name)

from moduleC import *
from moduleB import *
print(mutiply(5,2))
print(add(10,20))
print(subtract(30,20))
print(power(5,2))

print(name)
insert()
delete()
update()
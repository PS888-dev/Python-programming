# เจาะลึก string
# fname="เบศร"
# lname="จินดา"

# fullname=fname+lname+" หล่อไป"
# print(fullname)

# adress="""
# ที่อยู่ 123
# หมู่ 5
# ซอย 1/2
# จังหวัด ปราจีนบุรี
# 25000
# """

# print(adress)

# year=2551
# salary=25000
# message=f"เกิดเมื่อปี พ.ศ. {year}"
# age=f"ปีนี้คุณมีอายุ {2569-year} ปี"
# data=f"เงินเดือนของผม = {salary:.2f} บาท"
# print(message)
# print(age)
# print(data)

# text="HelloPython"
# print(text[3:7]) 

# ฟังก์ชันจัดการสตริง
# print(name.startswith("นาย")) #upperพิมพ์ใหญ่/lowerพิมพ์เล็ก startswithตรวจสอบว่าข้อความขึ้นต้นด้วยคำที่กำหนดหรือไม่/endswithตรวจสอบว่าข้อความลงท้ายด้วยคำที่กำหนดหรือไม่
# name="นายพศวีร์ จินดาประเสริฐ"
# name=input("ป้อนชื่อของคุณ: ")
# if name.startswith("นาย"):
#     print("เป็นเพศชาย")
# elif name.startswith("นาง"):
#     print("เป็นเพศหญิง")

# endwith ตรวจสอบว่าข้อความลงท้ายด้วยคำที่กำหนดหรือไม่
# mount=input("ป้อนชื่อดือน")
# if mount.endswith("คม"):
#     print("เดือนนี่มี 31 วัน")
# elif mount.endswith("ยน"):
#     print("เดือนนี่มี 30 วัน")

# find ตรวจสอบว่ามีคำที่กำหนดอยู่ในข้อความหรือไม่ ถ้ามีจะคืนค่าเป็นตำแหน่งของคำที่พบ ถ้าไม่พบจะคืนค่าเป็น -1 count นับจำนวนคำที่กำหนดในข้อความ
text2="สวัสดี คุณป้า คุณน้า คุณตา คุณยาย"
print(text2.find("คุณ"))
# print(text.count("คุณ"))

#  replace แทนที่คำที่กำหนดด้วยคำใหม่
# text="สัญญาจ้างงานประจำปี 2568 มีผลตั้งแต่ มกราคม 2568 ถึงธันวาคม 2568"
# update=text.replace("2568","2569")
# print(update)

# strip ลบช่องว่างที่อยู่ข้างหน้าหรือข้างหลังข้อความ
# text="  python  ".strip() 
# print(len(text))

#format จัดรูปแบบข้อความ
# text="ฉันชื่อ {} อายุ {} ปี".format("เบศร","18")
# print(text)  
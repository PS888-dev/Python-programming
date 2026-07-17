


#Guard Filter การนำ match case statement ร่วมกับ if statement เพื่อกำหนดเงื่อนไขในการทำงาน
#100 = สอบได้คะแนนเต็ม , 50-99 = ผ่านเกณฑ์การสอบวัดผล
# score=int(input("ป้อนคะแนนสอบของคุณ:"))
# print("คะแนนของคุณ คือ ",score)
# match score:
#     case 100:
#         print("สอบได้คะแนนเต็ม")
#     case score if score >=50 and score < 100:
#         print("ผ่านเกณฑ์การสอบวัดผล")
#     case score if score>=0 and score<=49 : #ทำเอง ที่สอนใช้ case score _ : print("คะแนนไม่ได้อยู่ในเกณฑ์ที่กำหนด")
#         print("สอบไม่ผ่าน")
#     case score if score<0 or score>100 :
#         print("กรอกคะแนนไม่ถูกต้อง")


#OR Pattern | แทน or
# data = input("ป้อนคำนำหน้าชื่อของคุณ:")

# match data:
#     case "เด็กชาย" | "นาย" :
#         print("เป็นเพศชาย")
#     case "เด็กหญิง" | "นางสาว"| "นาง" :
#         print("เป็นเพศหญิง")
#     case _:
#         print("ไม่พบข้อมูล")

#Sequence Pattern กำหนดรูปแบบการทำงานลำดับ ใช้ () ,  [] ใช้ร่วมกันได้
# data=[1,2]
# match data:
#     case []:
#         print("ไม่มีข้อมูล")
#     case[1,2,]:
#         print("มีข้อมูล 2 รายการคือ 1 และ 2")
#     case [1,2,3]:
#         print("มีข้อมูล 3 รายการคือ 1, 2 และ 3")


#Mapping Pattern
# customers=[
#     {"name":"เมธ","type":"general"},
#     {"name":"ข้าว","type":"member"},
#     {"name":"ปุ้น","type":"general"}
# ]
# id=int(input("ป้อนรหัสลูกค้า:"))
# print(f"สวัสดีลูกค้ารหัส {id} :{customers[id]["name"]}")

# match customers[id]:
#     case {"type":"member"}:
#         print("คุณเป็นสมาชิกได้รับส่วนลด 50%")
#     case _:
#         print("ไม่ได้รับส่วนลด")


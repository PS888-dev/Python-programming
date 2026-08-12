#Leiteral Pattern ง่ายที่สุด เป็นการกำหนดในตัวเเปร ตัวเเปรค่าคงที่
# service = None
# match service:
#     case 1:
#         print("ฝากเงิน")
#     case 2:
#         print("ยอดเงินคงเหลือ")
#     case 3:
#         print("สอบถามยอดเงินคงเหลือ")
#     case None:
#         print("ข้อมูลไม่ถูกต้อง")

#Wildcard Pattern กำหนดเงื่อนไขไม่ตรงกับเงือนไขใดเลย
# service = 100
# match service:
#     case 1:
#         print("ฝากเงิน")
#     case 2:
#         print("ยอดเงินคงเหลือ")
#     case 3:
#         print("สอบถามยอดเงินคงเหลือ")
#     case _:#กรณีที่ค่าตัวแปรไม่ตรงกับค่าคงที่ที่กำหนดไว้
        # print("ข้อมูลไม่ถูกต้อง")

#Capture Pattern นำเอาช้อมูลมาเเจกเเจงรายระเอียด ค่าไม่ตรงกับอะไรเลย
# service = 0
# match service:
#     case 1:
#         print("ฝากเงิน")
#     case 2:
#         print("ยอดเงินคงเหลือ")
#     case 3:
#         print("สอบถามยอดเงินคงเหลือ")
#     case service: #ถ้าไม่ตรงวิ่งมาตรงนี้
#         print(f"ไม่มีบริการหมายเลข {service} ในระบบ")


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
#     # case score if score<0 or score>100 : #ยาว
#     #     print("กรอกคะแนนไม่ถูกต้อง")
#     case _ : #สั้น
#         print("กรอกคะแนนไม่ถูกต้อง")
        
        
#OR Pattern | แทน or เพิ่มเติม or ใช้สำหรับ if statement 
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


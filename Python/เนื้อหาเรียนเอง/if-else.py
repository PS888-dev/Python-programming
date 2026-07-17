# คำสั่งเงือนไข
score=int(input("กรุณาป้อนคะแนนสอบของคุณ:"))

print("คะแนนสอบของคุณ =",score,"คะแนน")

# process
if score<0:
   print("คะแนนไม่ถูกต้อง")
elif score>=50:
   print("A")
else:
   print("F")


# ternary operator if else แบบลดรูป
# number= int(input("กรุณาป้อนตัวเลขของคุณ:"))
# print("ตัวเลขของคุณ คือ ",number)
# print("เลขคู่") if number%2==0 else print("เลขคี่")


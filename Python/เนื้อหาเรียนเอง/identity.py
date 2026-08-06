#identity operator
colorsA=["สีแดง","สีเขียว","สีน้ำเงิน"]
colorsB=["สีแดง","สีเขียว","สีน้ำเงิน"]
data=colorsA
# is = เหมือน is not = ไม่เหมือน
print(colorsA is not colorsB) 
print(colorsA is data)

#membership operator
colors=["สีแดง","สีเขียว","สีน้ำเงิน"]
# in = มีอยู่ not in = ไม่มี
print("สีแดง" in colors) #เป็นสมาชิกมั้ย
print("สีดำ" not in colors) #ไม่ได้เป็นสมาชิกมั้ย
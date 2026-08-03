width = float(input("กรอกความกว้าง :"))
long1 = float(input("กรอกความยาว :"))
high = float(input("กรอกความสูง :"))
color=2.5

m2 = (width*high*2)+(long1*high*2)#หาพื้นที่
liter = m2/color
bath=liter*40

print(f"มีพื้นที่ {m2} ตารางเมตร")
print(f"ใช้สี {liter} ลิตร")
print(f"ต้องจ่าย {bath} บาท")
#list
# product=["กางเกง",99.99,10,True]

#แก้ไขข้อมูลใน list
# product[0]="เสื้อ"
# product[1]=250
#เข้าถึงสมาชิก
# print(product)

# colors1=["ดำ","แดง","เขียว","ดำ"]
# colors2=["ขาว","ฟ้า","ส้ม"]
# fullcolors=colors1+colors2
# print(fullcolors)

# colors=["แดง","เขียว","น้ำเงิน","ดำ","ขาว"]
# colors.sort() #เรียงลำดับสมาชิกใน list
# colors.reverse() #เรียงลำดับสมาชิกใน list แบบย้อนกลับ
# print(colors)
# colors.append("น้ำตาล") #เพิ่มสมาชิกใน list ตัวเดียว
# colors.extend(["ส้ม","เหลือง",]) #เพิ่มสมาชิกใน list แบบหลายตัว
# colors.insert(1,"เทา") #เพิ่มสมาชิกใน list แบบระบุตำแหน่ง
# colors.remove("น้ำเงิน") #ลบสมาชิกใน list แบบระบุชื่อ
# colors.clear()  #ลบสมาชิกใน list แบบลบทั้งหมด
#print(colors.count("แดง")) #นับจำนวนสมาชิกใน list

#tuple แก้ไขข้อมูลไม่ได้
# colors1=("แดง","เขียว","น้ำเงิน")
# colors2=tuple(("ดำ","ขาว"))

# fullcolors=colors1+colors2
# print(fullcolors*2) #การคูณ tuple จะทำให้สมาชิกใน tuple ซ้ำตามจำนวนที่กำหนด

# colors=("แดง","เขียว","น้ำเงิน","ดำ","ขาว")
# print(colors[1:3])
 
#set ข้อมูลไม่ซ้ำกัน และไม่มีลำดับ แก้ไขข้อมูลไม่ได้ ไม่เรียงลำดับ
animals={"หมา","แมว","สิงโต","เสือ","ช้าง"}
# print("หมา" in animals) #ตรวจสอบว่ามีสมาชิกใน set หรือไม่
animals.add("เป็ด") #เพิ่มสมาชิกใน set ตัวเดียว
animals.update(("หมู","ยีราฟ")) #เพิ่มสมาชิกใน set แบบหลายตัว

# pet=set(("หมา","แมว","กระต่าย","เม่น"))
# print(animals)
# print(pet)

# data=animals.union(pet) #union รวมสมาชิกใน set ทั้งสองแบบไม่ซ้ำกัน
# print(data)

# data=animals.intersection(pet) #intersection หาสมาชิกที่ซ้ำกันใน set ทั้งสอง
# print(data)

# data=animals.difference(pet) #difference หาสมาชิกที่ไม่ซ้ำกันใน set ทั้งสอง
# print(data)

#dictionary ข้อมูลแบบคู่คีย์-ค่า แก้ไขข้อมูลได้ ไม่มีลำดับ 
colors={
    "red":"แดง",
    "green":"เขียว",
    "blue":"น้ำเงิน"
    }
# colors["yellow"]="เหลือง" #เพิ่มสมาชิกใน dictionary
# colors["blue"]="คราม"   #แก้ไขข้อมูลใน dictionary แบบระบุคีย์


print(colors.keys()) #แสดงคีย์ใน dictionary
print(colors.values()) #แสดงค่าใน dictionary
print(colors.items()) #แสดงคู่คีย์-ค่าใน dictionary

# print(colors["red"]) #ทำงานเหมือนกันกับอันล่าง
# print(colors.get("red")) #เข้าถึงค่าของคีย์ใน dictionary แบบระบุคีย์
maincolors=colors.copy() #คัดลอก dictionary ก่อนแก้ไขข้อมูล
# colors.pop("blue") #ลบสมาชิกใน dictionary แบบระบุคีย์
# colors.clear() #ลบสมาชิกใน dictionary แบบลบทั้งหมด
# colors.update({"yellow":"เหลือง","pink":"ชมพู"}) #เพิ่มสมาชิกใน dictionary แบบหลายตัว
# colors.update({"red":"แดงเข้ม"}) #แก้ไขข้อมูลใน dictionary แบบระบุคีย์

# print(colors)
# print(maincolors) 
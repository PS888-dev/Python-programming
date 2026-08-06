#list
# product=["กางเกง",99.99,10,True]
# # product=list(("กางเกง",99.99,10,True))

# # แก้ไขข้อมูลใน list
# product[0]="เสื้อ"
# product[1]=250
# # เข้าถึงสมาชิก
# print(product[0]) #เข้าถึงสมาชิกใน list แบบระบุตำแหน่ง
# print(product)

# colors1=["ดำ","แดง","เขียว","ดำ"]
# colors2=["ขาว","ฟ้า","ส้ม"]
# fullcolors=colors1+colors2
# print(fullcolors)

# number = ["50,20,10,23,160"]
# colors=["แดง","เขียว","น้ำเงิน","ดำ","ขาว"]
# colors.sort() #เรียงลำดับสมาชิกใน list
# number.sort() #เรียงลำดับสมาชิกใน list
# colors.reverse() #เรียงลำดับสมาชิกใน list แบบย้อนกลับ
# number.reverse() #เรียงลำดับสมาชิกใน list แบบย้อนกลับ
# print(colors)
# print(number)
# colors.append("น้ำตาล") #เพิ่มสมาชิกใน list ตัวเดียว
# colors.extend(["ส้ม","เหลือง",]) #เพิ่มสมาชิกใน list แบบหลายตัว
# colors.insert(1,"เทา") #เพิ่มสมาชิกใน list แบบระบุตำแหน่ง
# colors.remove("น้ำเงิน") #ลบสมาชิกใน list แบบระบุชื่อ
# colors.clear()  #ลบสมาชิกใน list แบบลบทั้งหมด
#print(colors.count("แดง")) #นับจำนวนสมาชิกใน list

# tuple ไม่สามารถเเก้ไขข้อมูลได้
# product=("กางเกง",150.0,10)
# name,price,stock, = product
# # print(type(product))
# print(name)
# print(price)
# print(stock)

# colors = ("เเดง","เขียว","น้ำเงิน","ดำ","ขาว")
# colors2 =tuple(("ดำ","ขาว"))

# fullcolors=colors1+colors2
# print(type(fullcolors))
# print(fullcolors)
# print(colors[0:])
# print(colors.index("ดำ")) #หาข้อมูลสมาชิกในข้อมูล
# print(colors.count("เเดง")) #หาว่ามีข้อมูลกี่ตัว

# # set ต้องมีต่าไม่ซ้ำกัน มีลำดับไม่ชัดเจน
# animals = {"หมา","เเมว","สิงโต","เสือ"}
# # animals.add("เป็ด") #ต้องการเพิ่มเข้าไปในsetเเบบเดี่ยว
# # animals.update("ปลา","ลิง") #ต้องการเพิ่มเข้าไปในsetเเบบหลายอัน

# pet=set(("หมา","เเมว","เม่น","กระต่าย"))
# print(pet)
# print(animals)
# # print("หมา" in animals) #หาว่ามีค่าในsetหรื่อไม่

# data=animals.union(pet) #การเอาสมาชิกทุกตัวมารวมกัน
# data=animals.intersection(pet) #การเอาสมาชิกเหมือนกันมาใช้
# data=animals.difference(pet) #set ใช้สำหรับ หาสมาชิกที่มีอยู่ในเซตแรก แต่ไม่มีอยู่ในเซตที่สอง
# print(data)

#dictionary
colors={
    "red":"เเดง", #ข้างหน้าคือkey ข้างหลังคือ value
    "green":"เขียว",
    "blue":"น้ำเงิน"
}
# print(colors.keys()) #ดูว่าใน Dictionary มี คีย์ (Key) อะไรบ้าง
# print(colors.values()) #ดึง ค่าของข้อมูล (Value) ออกมา โดยไม่แสดงชื่อkey
# print(colors.items()) #ดึง ค่าของข้อมูล มาทั้งคู่
# print(colors["red"]) #ใช้สำหรับ ดึงค่าจากคีย์ same
# print(colors.get("red")) #ใช้สำหรับ ดึงค่าจากคีย์ same
# colors.pop("blue") #ต้องการลบkeyที่จะลบทิ้ง ลบข้อมูลที่ละรายการ
# colors.clear() #ลบข้อมูลทั้งหมดของ colors
# print(colors)
# maincolor=colors.copy() # การcopyจากอีกที่นึง
# colors.update({"yellow":"เหลือง"}) # การเพิ่มข้อมูลเข้าไปใน dic
# colors.update({"yellow":"เหลืองอ่อน"}) # การเเก้ไข

# print(colors)
# print(maincolor)
# for key,value in colors.items():
#     print(key,"=",value)


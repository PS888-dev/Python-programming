#สร้างFunction
# def sayHello(time,username,age): #Parameterรับ คืออยู่ในวงเล็บ
#     print("สวัสดี",time,username)
#     print("ปีนี้คุณมีอายุ",age, "ปี")

# def saveEmployee(name,department,salary=15000,address): #Default คือ salary=15000
#     print(f"ชื่อ{name}, แผนก{department}")
#     print(f"เงินเดือน {salary} บาท")
#     print(f"ที่อยู่ {address} ")
#     print("-------------")

# def showTable(num):
#     print(f"------แม่ {num}------")
#     for i in range (1,13):
#         print(f"{num} x {i} = {num*i}")


#เรียกใช้งาน
# myTime="ตอนเช้า"
# sayHello("ตอนบ่าย","คุณเมธ",30) #argumentส่ง อยู่ในวงเล็บ
# sayHello(myTime,"คุณปุ้น",18)
# showTable(2)

#argument args ใช้ * เป็นแบบลำดับ ไม่จำเป็นต้องใช้ชื่อargs อยู่ในรูปแบบtuple จำลำดับ0,1 , kwargs ใช้ ** เป็นแบบกำหนดชื่อ ไม่จำเป็นต้องใช้ชื่อlkwargs อยู๋ในรูปแบบdictionary ใช้keysแทน
# def saveEmployee(*args):
#     print(f"ชื่อ{args[0]}, แผนก{args[1]}")
#     print(f"เงินเดือน {args[2]} บาท")
#     print(f"ที่อยู่ {args[3]}")
#     print("-------------")
    
# def saveEmployee(**kwargs):
#     print(f"ชื่อ{kwargs["name"]}, แผนก{kwargs["department"]}")
#     print(f"เงินเดือน {kwargs["salary"]} บาท")
#     print(f"ที่อยู่ {kwargs["country"]}")
#     print("-------------")

#Parameter คือตัวแปรรับ argument คือตัวแปรส่ง
# *args ข้อมูลเเบบดำลับ
# saveEmployee("เบส","ไอที",30000,"ปราจีนบุรี")
# saveEmployee("ปุ้น","ผลิตยาม้า",1000000,"กรุงเทพฯ")
# saveEmployee("เมธ","ไอที",30000,"ชลบุรี")

# **kwargs ข้อมูลเเบบกำหนดชื่อ กำหนดkeyเข้าไป
# saveEmployee(name="เบส",department="ไอที",salary=30000,country="ปราจีนบุรี")
# saveEmployee(name="ปุ้น",department="ผลิตยาม้า",salary=1000000,country="กรุงเทพฯ")
# saveEmployee(name="เมธ",department="ไอที",salary=30000,country="ชลบุรี")
# saveEmployee("เด็กใหม่","บัญชี") #salary = 15000 เพราะเป็นค่าเริ่มต้นที่กำหนดไว้
#Function Default(ค่าเริ่มต้น) กำหนดค่าเริ่มต้น ใส่=


# return function
# def getCapital():
#     return "กรุงเทพฯ"

# def getPI():
#     return 3.14
# area = PI * radius ^2
# radius=5
# area= getPI()*radius**2
# print("พื้นที่ลงกลม =", area, "ตารางเมตร")

# myData = getCapital()
# print("เมืองหลวงของฉันคือ",myData)


# para + return function
def checkNumber(number):
    if number%2==0:
        return "เลขคู่"
    else:
        return "เลขคี่"
    
def summation(*data):
    total=0
    for item in data:
        total+= item
    return total
    
# result= checkNumber(10)
# print("ผลลัพธ์ =", result)
print(summation(10,20))
print(summation(10,20,30))


#Lambda fuction สั้นกระชับ
# result= lambda base,n: base**n
# print("ผลลัพธ์", result(2,3))


#ขอบเขตตัวแปร Variable scop and return keyword
# balance=1000 #global ทำงานนอกfuction 
# def displaybalance():
#     print("ยอดเงินคงเหลือในบัญชี", balance, "บาท")

# def deposit(value): #value มีdeposit เป็นเจ้าของ ทำงานได้แค่ในนี้
#     global balance #ต้องประกาศตัวแปร global เข้ามาในfuction ถึงจะใช้งานร่วมกันได้
#     money=value
#     print("ฝากเงินจำนวน",money, "บาท")
#     if(money<=0 or money<100):
#         print("ไม่สามารถฝากเงินได้")
#         return #ตรงตามเงื่อนไขข้างบนจะกระโดดออกจากโค๊ดตัวล่าง
#     balance+=money
   

# def withdraw(value): #value มีwithdraw เป็นเจ้าของ ทำงานได้แค่ในนี้
#     global balance #ต้องประกาศตัวแปร global เข้ามาในfuction ถึงจะใช้งานร่วมกันได้
#     money=value
#     amont=value
#     print("ถอนเงินจำนวน",amont, "บาท")
#     if amont<=0 or amont>balance or amont<100:
#         print("ไม่สามารถถอนเงินได้")
#         return
#     balance-=amont

# displaybalance()
# deposit(100)
# withdraw(900)
# displaybalance()

#Exception try คือ ลองทำคำสั่งในนี้ except คือ ถ้าเกิดข้อผิดพลาดจะมาทำงานตรงนี้ finally คือ คำสั่งต่างๆ
# try:
#     number1=int(input("ป้อนตัวเลขที่ 1 :"))
#     number2=int(input("ป้อนตัวเลขที่ 2 :"))
#     if number1<0 or number2<0:
#         raise Exception("ข้อมูลตัวเลขต้องเป็นค่าบวกเท่านั้น!")
        
#     result = number1/number2
#     print("ผลลัพธ์ = ",result)
# except ValueError:
#     print("ข้อมูลไม่ถูกต้อง กรุณาป้อนข้อมูลเฉพาะตัวเลขเท่านั้น!")
# except ZeroDivisionError:
#     print("หารด้วยศูนย์ไม่ได้! เนื่องจากไม่ถูกนิยามในคณิตศาสตร์")

# finally:
#     print("------------")
#     print("End Program")
#     print("------------")



name = (input("ชื่อพนักงาน :"))
income = int(input("รายได้ :"))
tax1,tax2 = 0.05,0.10
print("*"*20)
if income <= 500000:
    tax1=income*tax1
    print(f"เสียภาษี :{tax1}\nรายได้บริสุทธ์ :{income-tax1}")

elif income > 500000:
    tax1=income*tax2
    print(f"เสียภาษี :{tax1}\nรายได้บริสุทธ์ :{income-tax1}")
print("*"*20)
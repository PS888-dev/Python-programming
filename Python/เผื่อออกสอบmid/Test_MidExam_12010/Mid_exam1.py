# นายพศวีร์ จินดาประเสริฐ 6906021612010

number = int(input(f"{" "*5}กรอกเเม่สูตรคูณ (2-12) : "))
if number <= 12:
    print(f"{" "*8}ตารางเเม่สูตรคูณ {number}")
    print(f"-"*32)
    for i in range(1,13,+1):
        print(f"{" "*10}{number} x {i} = {i*number}")
else:
    print(f"กรุณากรอกเลขระหว่าง 2 ถึง 12")
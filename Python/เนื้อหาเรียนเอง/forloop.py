# สำหรับเงื่อนไขรู้รู้ค่าเเล้ว

for counter in range(10): #0-9
   print(counter)
for counter in range(1,5): #1-4
   print(counter)
for counter in range(1,5,2): #เพิ่มทีละ 2
      print(counter)


# break หยุดการทำงานเลย/continue ข้ามไปทำงานอีกตัวเลย
for counter in range(1,11):
    if counter%2==0:
        continue 
    print(counter)

print("จบการทำงาน")
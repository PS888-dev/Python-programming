# นายพศวีร์ จินดาประเสริฐ 6906021612010

print(f"Input Data:")
report = (f"{" "*30}Grade Report")
bar = (f"{"="*64}")
title = (f"Sub No.   Subject Name          Mark   Grade   Credits   Points")
total_point = 0
total_credit = 0
credit = 3
total_all =""

for i in range(1,6):
    subject,score = input(f"Enter subject name({i}): "),int(input(f"Enter subject score({i}): "))
    print()
    
    if score >= 80: grade, level = "A", 4.0
    elif score >= 70: grade, level = "B", 3.0
    elif score >= 60: grade, level = "C", 2.0
    elif score >= 50: grade, level = "D", 1.0
    else: grade, level = "F", 0
    
    point = level * credit
    total_point += point            # บวกสะสมคะแนนรวม
    total_credit += credit          # บวกสะสมหน่วยกิตรวม
    total_all += f"  {i:<6} {subject:<21}  {score:<5.1f}   {grade:>3}      {credit:^5}   {int(point):>6} \n"
total_all += f"{bar}\n {"Total":>36}  {int(total_point):>13}{int(total_credit):>11}\n"
total_all += f"{bar}\nGrade Point Average (GPA) :  {total_point/total_credit:.2f}"

print(f"{report}\n{bar}\n{title}\n{bar}")
print(total_all)


# print(len("Sub No. Subject           Name   Mark   Grade   Credits   Points"))
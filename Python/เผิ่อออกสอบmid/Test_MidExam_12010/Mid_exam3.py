# # นายพศวีร์ จินดาประเสริฐ 6906021612010

report = (f"{" "*30}Report Grade")
bar = (f"{"="*76}")
title = (f"| No. |{" "*7}Name Subject{" "*7} | Socre | Grade | Level | Credit | Point |")
total_point = 0
total_credit = 0
total_all =""
for i in range(5):
    subject,score,credit = input("วิชา: "),int(input("คะเเนน : ")),int(input("หน่วยกิต : "))
    
    if score >= 80 and score <= 100 :grade, level = ("A"), 4.0
    elif score >= 75 and score <= 79:grade, level = ("B+"), 3.5
    elif score >= 70 and score <= 74:grade, level = ("B"), 3.0
    elif score >= 65 and score <= 69:grade, level = ("C+"), 2.5
    elif score >= 60 and score <= 64:grade, level = ("C"), 2.0
    elif score >= 55 and score <= 59:grade, level = ("D+"), 1.5
    elif score >= 50 and score <= 54:grade, level = ("D"), 1.0
    else: grade, level = ("F"), 0.0
    i += 1
    total_point = level * credit
    total_credit = total_point / credit
    total_all += f"|  {i}  | {subject:<25} | {score:>3}   | {grade:>3}   | { level:^6}| {credit:^5}  | {total_point:^5.1f} |\n"
total_all += f"{bar}\n| {"Total":^55} | {total_point:^7}|{total_credit:^7}|\n"
total_all += f"{bar}\n|{"Grade Point Average (GPA) : ":>50} {total_point/total_credit:.2f}{"|":>20}\n{bar}"

print(f"{report}\n{bar}\n{title}\n{bar}")
print(total_all)






# print(len("| No. |       Name Subject        | Score | Grade | Level | Credit | Point |"))

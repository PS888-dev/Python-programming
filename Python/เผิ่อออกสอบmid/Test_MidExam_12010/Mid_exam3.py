# # นายพศวีร์ จินดาประเสริฐ 6906021612010
print(f"{" "*30}Report Grade")
print(f"{"="*74}")
print(f"| No. |{" "*6}Name Subject{" "*6} | Socre | Grade | Level | Credit | Point |")

for i in range(1,6,+1):
    subject = input(f"|  {i}  |")
    score = int(input(f"คะเเนน : "))
    i += 1
    
    if score >= 80 and score <= 100 :Grade=("A")
    elif score >= 75 and score <= 79:print("B+")
    elif score >= 70 and score <= 74:print("B")
    elif score >= 65 and score <= 69:print("C+")
    elif score >= 60 and score <= 64:print("C")
    elif score >= 55 and score <= 59:print("D+")
    elif score >= 50 and score <= 54:print("D")
    elif score >= 0 and score <= 49:print("F")
    else:print("กรอกคะเเนนไม่ถูกต้อง")
    
# print(f"{" "*30}Report Grade")
# print(f"{"="*74}")
# print(f"| No. |{" "*6}Name Subject{" "*6} | Socre | Grade | Level | Credit | Point |")

# print(f"{i}")

# print(len("| No. |       Name Subject        | Score | Grade | Level | Credit | Point |"))

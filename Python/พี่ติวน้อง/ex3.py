#โปรแกรมตัดเกรด
#input
name = input("Enter You Name : ")
score = int (input ("Enter You Score (0-100) : "))
grade=""

#pocess
if score >= 80 and score <= 100: grade = "A"
elif score >= 75 and score < 79: grade = "B+"
elif score >=70 and score <=74: grade = "B"
elif score >=65 and score <=69: grade = "c+"
elif score >=60 and score <=64: grade = "c"
elif score >=55 and score <=59: grade = "D+"
elif score >=50 and score <=54: grade = "D"
elif score >=45 and score <=49: grade = "F"
else:grade="N (Invalid)"

#output
print("="*25)
print("Name : ", name)
print("="*25)
print("Score : ", score)
print("="*25)
print("Score  : You : Grade ", grade)
print("="*25)
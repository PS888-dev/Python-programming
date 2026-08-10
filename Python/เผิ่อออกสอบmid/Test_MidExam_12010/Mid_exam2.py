# นายพศวีร์ จินดาประเสริฐ 6906021612010
total = 0
for i in range(1,6,+1):
    number1 = int(input(f"Enter number #{i} : "))
    total += number1

print(f"{"="*21}\nTotal = {total}\n{"="*21}\nAverage = {total/i:,.2f}\n{"="*21}")
qty = int(input("Enter number product : "))
price = float(input("price per unit : "))

total = price  * qty
print("Total money : " ,total)

pay = float(input("Enter pay monry :"))
change = pay - total
print("Money change : ",change)
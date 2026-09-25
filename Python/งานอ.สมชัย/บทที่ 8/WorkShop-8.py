from random import randint

def inputSales(sales):
    for n in range(1,5):
        key = input("Enter branch name : ")
        value = []
        for m in range(1,5):
            data = float(input(f"Enter sales in Quarter {m} :"))
            value.append(data)
        sales[key] = value

def calTotalSales(sales):
    for key in sales:
        sales[key].append(sum(sales[key]))

def reportSales(sales):
    result = ("="*76)+"\n"+"| No. | Branch Name | Quarter1 | Quarter2 "
    result += "| Quarter3 | Quarter4 |   Total   |\n"+("="*76)+"\n"
    n = 1
    for key in sales:
        result += f"|  {n:2} | {key:11}  |"
        for sale in sales[key]:
            result += f" {sale:8.2f} |"
        result += "\n"
        n = n+1
    result += ("="*76)+"\n"
    print(result)

salesData = {}
inputSales(salesData)
calTotalSales(salesData)
reportSales(salesData)
for key in salesData:
    print(key, salesData[key])
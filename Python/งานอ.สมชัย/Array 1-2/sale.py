import random
def Init() :
    return 0

def Read(sales) :
    for n in range(15) :
        sales.append( random.randint( 10, 99) ) 
    return sales

def Calc(sales,percents,total) :
    total = sum(sales)
    for sale in sales:
        percents.append((sale / total) * 100 if total != 0 else 0)
    return percents

def Print(sales, percents) :
    line = "+"+("-"*23) +"+\n"
    result = line+"| No.|  Sales  | Percent |\n"+line
    for i in range(15):
        result +=f"| {i + 1:2} | ${sales[i]:6.2f} | {percents[i]:6.2f}% |\n"
    result += line
    print(result)

# Main Program
total = Init()
sales = []
percents = []
sales = Read(sales)
percents = Calc(sales, percents, total)
Print(sales, percents)
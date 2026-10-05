import random
def Init() :
    sales = []
    for r in range(16) :
        sales.append( [] )
        for c in range(8) :
            sales[r].append( 0 )
    return sales

def Read(sales) :
    for r in range(15) :
        for c in range(7) :
            sales[r][c] = random.randint( 1, 100 )
    #return sales

def Calc(sales) :
    for r in range(15) :
        for c in range(7) :
            sales[r][7] += sales[r][c] # ผลรวมแนวแถว
            sales[15][c] += sales[r][c] # ผลรวมแนวคอลัมน์
        sales[15][7] += sales[r][7] # ผลรวมทั้งหมด
    #return sales

def Print(sales) :
    line = "+"+ ("-"*72)+"+\n"
    result = line
    result += "|  No. |  Day1 |  Day2 |  Day3 |  Day4 |  Day5 |  Day6 |  Day7 |  Total  |\n"
    result += line
    for r in range(16):
        result += f"|  {r + 1:2}  |" if r < 15 else line+"| Total|"
        for c in range(8):            
            result += f"{sales[r][c]:7.2f}|" if c < 7 else f"{sales[r][c]:9,.2f}|"
        result += "\n"

    result += line
    print(result)

# Main Program
sales = Init()
Read(sales)
Calc(sales)
#print(sales)
Print(sales)
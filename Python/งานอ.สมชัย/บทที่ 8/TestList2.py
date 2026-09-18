import random

def randomTemparature(temps):
    for r in range(7):
        temps.append([])
        for c in range(4):
            temps[r].append(random.randint(20,40))
        

def sumTemperature(temps):
    for r in range(len(temps)): #row
        total = 0
        for c in range(len(temps[r])-1): #colum
            total += temps[r][c]
        temps[r][3] = total / 3


def reportTemparature():
    line = ("-"*42) +"\n"
    result = "\n" + "Report of Temperature in Prachinbury".center(42) + "\n"
    result += line + "|Area|  Day1  |  Day2  |  Day3  | Average|\n" + line
    for r in range(len(temps)):
        result += f"|{r+1:3} |"
        for c in range(len(temps[r])):
            result += f" {temps[r][c]:6.2f} | "
        result += f"\n"    
    result += ("-"*42)
    print(result)

temps = []

randomTemparature(temps)
sumTemperature(temps)
reportTemparature()
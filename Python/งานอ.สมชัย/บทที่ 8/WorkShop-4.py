import random

def randomTemparature(day1, day2, day3,):
    for n in range(1,8):
        day1.append(random.randint(20,40))
        day2.append(random.randint(20,40))
        day3.append(random.randint(20,40))

def sumTemperature(day1, day2, day3, avg):
    total = 0
    for n in range(len(day1)):
        total = day1[n] + day2[n] + day3[n]
        avg.append(total/3)

def repotTemparature():
    line = ("-"*42) +"\n"
    result = "\n" + "Report of Temperature in Prachinbury".center(42) + "\n"
    result += line + "|Area|  Day1  |  Day2  |  Day3  | Average|\n" + line
    for n in range(len(day1)):
        result += f"|{n+1:3} | {day1[n]:6.2f} | {day2[n]:6.2f} "
        result += f"| {day3[n]:6.2f} | {avg[n]:6.2f} | \n"
    result += ("-"*42)
    print(result)

day1 = []
day2 = []
day3 = []
avg = []
randomTemparature(day1, day2, day3)
sumTemperature(day1,day2,day3,avg)
repotTemparature()
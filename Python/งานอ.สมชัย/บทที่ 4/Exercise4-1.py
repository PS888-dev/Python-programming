print(">>  Program Find Maximum Digit  <<")
number=0
while True:
    number=int(input("Enter integer number (0-exit) : "))
    print(f"Maxumum Digit of intiger number {number} = {max(int(number))} ")
    if number<=0:
        break
print("Exit program")
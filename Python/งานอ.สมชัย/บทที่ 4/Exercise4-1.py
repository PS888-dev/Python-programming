print(">>  Program Find Maximum Digit  <<")
number=0
while True:
    number=int(input("Enter integer number (0-exit) : "))

    if number<=0:
        break
    
    max_digit=0
    for i in str(number):
        if int(i) > max_digit:
            max_digit=int(i)
            
    print(f"Maxumum Digit of intiger number {number} = {max_digit} ")
print("Exit program")

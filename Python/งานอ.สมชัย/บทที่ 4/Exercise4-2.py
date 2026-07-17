print(">> Program Find Maximum Digit <<")

while True:
    value = int(input("Enter number of value(>=1) : "))

    if value <= 0:
        print("value input not correct.")
        break

    print(f"\nProgram get value {value} numbers.")

    for i in range(1, value + 1):
        num = int(input(f"Enter value Number #{i} : "))
            
        # if i == 1:
            # print("Your enter number : ", num)
            # print("Maximum number is : ", num)
        

print("Exit program")
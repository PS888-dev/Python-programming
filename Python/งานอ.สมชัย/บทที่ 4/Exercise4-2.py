print(">> Program Find Maximum Digit <<")

value = int(input("Enter number of value(>=1) : "))

if value <= 0:
    print("value input not correct.")
else:
    num1=[]
    print(f"\nProgram get value {value} numbers.")

    for i in range(1, value + 1):
        num = int(input(f"Enter value Number #{i} : "))
        num1.append(num)

print("Your enter number : ",",".join(str(n) for n in num1))

max_num = max(num1)
    
print("Maximum value number is : ", max_num)
print("Exit program")
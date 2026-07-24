message = ""
maxValue = 5
count = 1
while count <= maxValue:
    s = input(f"Enter string #{count} : ")
    message += s + "\n"
    count += 1
    
print("\nPrint you string enter : ")
print(message)
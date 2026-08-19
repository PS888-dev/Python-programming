bar = "="*15
print(f"{bar}\n|  Main Menu  |\n{bar}")
print(f''' 1.  Triangle 1
 2.  Triangle 2
 3.  Triangle 3
 4.  Triangle 4
 5.  Exit''')


choice = input("Enter Choice : ")
match choice :
    case "1":
        print()
        n = int(input("Enter number of character : "))
        print()
        i = 1
        while i <= n:
            print("*"*i)
            i += 1
    case "2":
        print()
        n = int(input("Enter number of character : "))
        print()
        i = 1
        while i <= n:
            print("*"*(n-i+1))
            n -= 1
    case "3":
        print()
        n = int(input("Enter number of character : "))
        print()
        i = 1
        while i <= n:
            print(" " * (n - i) + "*" * i)
            i += 1
    case "4":
        print()
        n = int(input("Enter number of character : "))
        print()
        i = n
        while i >= 1:
            print(" " * (n - i) + "*" * i)
            i -= 1
    case "5":
        print()
        print("Exit Program ...")
    case _:
        print()
        print("Input error choice.")
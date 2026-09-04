def factorial1 (number):
    fac = 1
    for n in range(1,number+1):
        fac = fac * n
    return(fac)

def factorial2 (number):
    if number > 0:
        return(number*factorial2(number-1))
    else:
        return(1)

num = int(input("Enter number : "))
print("factorial1 with for = ", factorial1(num))
print("factorial2 with recursive = ", factorial2(num))

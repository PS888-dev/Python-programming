n=int(input("Enter a number: "))

num1=n//1000
n=n%1000

num2=n//100
n=n%100

num3=n//10
n=n%10

num4=n//1
n=n%1

sum=num1+num2+num3+num4

print()
print("The digits are: ",num1, num2, num3, num4)
print("The sum of the digits is:",sum)
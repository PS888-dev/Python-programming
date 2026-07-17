amount,rate,year,=int(input("Enter amount : ")),float(input("Enter rate : "))/100,int(input("Enter year : "))

fv1=amount*(1+rate)**year
print("Future value = ",fv1)
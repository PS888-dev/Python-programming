total=int(input("Total Bill (Baht): "))
number=int(input("Number fgo people: "))
service=number*0.1

print(f"="*6," Bill Summary ","="*6)

netprice=service+total
person=total/number

print()
print(f"Original Bill     : {total:,.2f} Baht")
print(f"Service Charge    : {service:,.2f} Baht")
print(f"Total Net Price   : {netprice:,.2f} Baht")
print(f"Each Person Pays  : {person:,.2f} Baht")
print("="*26)
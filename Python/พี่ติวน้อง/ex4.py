kwh = int(input("Enter electricity used (kWh) : "))
type1 = input("Enter user type (home / dorm / shop): ")

cost=8*kwh
charge=0

if type1 == "home":
    charge = 10
elif type1 == "dorm":
    charge = 15
elif type1 == "shop":
    charge = 20


print("="*25)
print(f"Electricity cost = {cost:.2f}" )
print("="*25)
print(f"Sevice charge {charge:.2f}")
print("="*25)
print(f"Total bill {cost+charge:.2f}")
print("="*25)
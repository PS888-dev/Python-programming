print("Data inputs are integer!.")
km=int(input("Enter the starting kilometers: "))
km2=int(input("Enter the ending kilometers: "))
time=int(input("Enter the time in hours: "))

km3=km2-km
km=km3/time
print()
print("The distance is: ", km3,"km")
print("The average speed is: ", km, "km/h")
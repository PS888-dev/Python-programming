import random
# ไม่ใช้ for loop
a = random.uniform(30.00,50.00)
b = random.uniform(30.00,50.00)
c = random.uniform(30.00,50.00)
d = random.uniform(30.00,50.00)
e = random.uniform(30.00,50.00)
print(f"value Random : {a:.2f} , {b:.2f} , {c:.2f} , {d:.2f} , {e:.2f}")
print(f"Total Value : {a+b+c+d+e:.2f}")
print(f"Average value : {(a+b+c+d+e)/5:.2f}")

#ใช้ for loop
n = 5
total = 0
sep = ""
print(f"value Random : ", end="")

for i in range(n):
    val = random.uniform(30.00, 50.00)
    total += val
    print(f"{sep}{val:.2f}", end="")
    sep = " , "
    
print(f"\nTotal Value : {total:.2f}")
print(f"Average value : {total/n:.2f}")
import math
print()
print("="*40)
print("|Angle|   sin   |   Cos   |   Tan   |")
print("="*40)
for angle in range(0,361,20):
    radian = math.radians(angle)
    print(f"|%4d |"  % angle,end="")
    print(f"|%9.5f |"  % math.sin(radian),end="")
    print(f"|%9.5f |"  % math.cos(radian),end="")
    print(f"|%9.5f |"  % math.tan(radian))
print("="*40)

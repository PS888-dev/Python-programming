total = 0.0
score = 1
count = 0
while score > 0:
    score = int(input("Enter score value  #" + str(count + 1) +  " : "))
    if score > 0:
        count += 1
        total += score

print()
print("Number of socre : ", count)
print("Total score value : ", total)
print("Average score : ", total / count)
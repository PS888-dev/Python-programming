total = 0.0
Max = int(input("Enter max of score : "))
for n in range(1, Max+1):
    score = float(input("Enter score #" + str(n) + " : "))
    # score = float(input(f"Enter score #{n} : "))
    total = total + score
print()
print("Total score value : ", total)
print("Average score : ", total / Max)
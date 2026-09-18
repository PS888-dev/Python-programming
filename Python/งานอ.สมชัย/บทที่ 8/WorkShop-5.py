from random import randint

student = int(input("Enter number of student : "))
subject = int(input("Enter number of student : "))

scores = []

for r in range(student):
    scores.append([])
    for c in range(student):
        scores[r].append(randint(0,100))
print()
print(scores)
print()

for score in scores:
    print(score)
    
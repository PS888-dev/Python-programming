def getPoint(grade):
    grades = ("A","B","C","D","F")
    values = (4,3,2,1,0)
    for n in range(len(grades)):
        if grade == grades[n]:
            return(values[n])

Done = True
while Done:
    grade = input("Enter grade (Q-exit): ").upper()
    if grade == "Q":
        Done = False
    elif grade in ("A","B","C","D","F"):
        value = getPoint(grade)
        print(f"Point value of {grade} is {value}")
    else:
        print("No grade, please input again.")

print("End Program.")
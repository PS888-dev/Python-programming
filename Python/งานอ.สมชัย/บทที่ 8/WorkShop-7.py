from random import randint

def randomScore(score):
    for n in range(1,31):
        score[n] = randint(30,100)

def checkGrade(score, grades):
    GRADES = {80:"A",70:"B",60:"C",50:"D",0:"F"}
    for n, score in score.items():
        for key, grade in GRADES.items():
            if (score >= key):
                grades[n] = grade
                break

def reprotGrade(scores,grades):
    result = ( "="*23 ) +"\n| No. | Score | Grade |\n"+( "="*23 )+"\n"
    for n in scores:
        result += f"|  {n:3}  |  {scores[n]:3}  |  {grades[n]:2} |\n"
    result += ("="*23)+"\n"
    print(result)

def FD(grades):
    fd = {"A":0, "B":0, "C":0, "D":0, "F":0}
    for grade in grades.values():
        fd[grade] += 1
    print(fd)

scores = {}
grades = {}
randomScore(scores)
print(scores)
checkGrade(scores,grades)  
print(grades)
reprotGrade(scores,grades)

FD(grades)
#Grading System

#Static Data = 
students = {
    "Prestige":{"Math": 80, "Eng": 70, "Art": 90},
    "Royal":{"Math": 90, "Eng": 80, "Art": 70},
    "Treasue":{"Math": 80, "Eng": 70, "Art": 90}
}

#Funtion to calculate grade
def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"
    
#Print Student Grades
for student, score in students.items():
    print(f"Students:{students}")
    for subject, score in score.items():
        grade = calculate_grade(score)
        print (f"{subject}: {score} ({grade})")
    print()
    
    
    
    
    
    
    #input Specified
while True:
    name = input("Enter student name (or 'q' to quit):")
    if name.lower() =='q':
        break
    scores = {}
    for subject in ["Math", "Eng", "Art"]:
        scores = int(input(f"Enter {subject} score for {name}: "))
        scores[subject] = score
    students[name] = scores
    for students, score in students.items():
        print(f"Student:{student}")
        for subject, score in scores.items():
             grade = calculate_grade(score)
             print(f"{subject}:{score} ({grade})")
             print()
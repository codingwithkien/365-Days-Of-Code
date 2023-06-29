print("====================================")
print("===== Rules for Grading System =====")
print("====================================")

TRY =  True
while TRY:
    name = input("What is your student name? ").title()
    class_name = int(input("Class Student: "))

    grade_score = float(input(f"Enter Grade of {name}: "))

    if grade_score <= 100:
        if grade_score >= 80:
            grade_string = "A"
        elif grade_score >= 60 and grade_score < 80:
            grade_string = "B"
        elif grade_score >= 50 and grade_score < 60:
            grade_string = "C"
        elif grade_score >= 45 and grade_score < 50:
            grade_string = "D"
        elif grade_score >= 25 and grade_score < 45:
            grade_string = "E"
        elif grade_score < 25:
            grade_string = "F"
        print(f"--> {name} is in class {class_name} have string grade: {grade_string} <--")
        print("-" * 20)
    else:
        print("Error! Please Enter Again.")
        print("-" * 20)



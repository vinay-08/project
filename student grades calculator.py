def calculate_sgpa(grades):
    total_credits = 0
    total_points = 0
    for grade in grades:
        course_credits = grade[0]
        course_grade = grade[1]
        total_credits += course_credits
        total_points += (course_credits * course_grade)
    print(total_points)
    print(total_credits)
    return total_points / total_credits

grades =[]
n=int(input("number of subjects: "))
for i in range(n):
    temp_list=[]
    course_credits=int(input("enter the credits for the subject: "))
    temp_list.append(course_credits)
    course_grade=input("Enter the grade secured: ")
    if course_grade == 'EX' :
        temp_list.append(int(10))
    elif course_grade == 'A' :
        temp_list.append(int(9))
    elif course_grade == 'B' :
        temp_list.append(int(8))
    elif course_grade == 'C' :
        temp_list.append(int(7))
    elif course_grade == 'D' :
        temp_list.append(int(6))
    elif course_grade == 'P' :
        temp_list.append(int(5))
    else :
        temp_list.append(int(0))
    grades.append(temp_list)
print(grades)
sgpa = calculate_sgpa(grades)
print(f"SGPA: {sgpa}")

# Addmission Process
# Colletcting Applicant details
candidate_name = input("Enter your Name: ").title()
age = int(input("Enter your Age: "))
utme_score = int(input("Enter your UTME Score: "))
university_choice = input("Did you choose UNILAG as your first choice\nYes or No: ").title()
post_utme = input("Did you participate in the university online Post-UTME Screening\nYes or No: ").title()
relevant_course = ["Mathematics", "English"]
print("Enter your other three O'level courses.")
# Collecting Applicant O'Level Details
number = 1
while True:
    olevel_result = input(f"{number}. ")
    if olevel_result in relevant_course:
        print(f"{olevel_result} already exist")
    else:
        relevant_course.append(olevel_result)
        number += 1
    if len(relevant_course) == 5:
        break
print(relevant_course)
grades = []
for subject in relevant_course:
    grade = input(f"Enter your grade in {subject}: ").upper()
    grades.append(grade)
# Checking Applicant Eligibility
if age >= 16 and university_choice == "Yes" and post_utme == "Yes" and utme_score >= 200:
    for grade in grades:
        grade_result = grade == "A" or grade == "B" or grade == "C"
        if grade_result == False:
            break
    if grade_result == True:
        print("Congratulation!!!\nYou have been addmited into the University of Lagos")
    else:
        print("You are not offered Addmission into the university of Lagos.")
else:
    print("You are not offered Addmission into the university of Lagos.")
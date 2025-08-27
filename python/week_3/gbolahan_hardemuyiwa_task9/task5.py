# Fedral Government Schorlarship Key Eligibility Requirement 
# citizenship = input("Are you a citizen of Nigeria?\nYes or No: ").title()
# enrollment = input("Are you registered as a full-time undergraduate student in a recognized nigerian university?\nYes or No: ").title()
# other_scholarships = input("Are you receiving any other scholarship from an entity in the Oil and Gas industry, whether national or internaltional?\nYes or No: ").title()
# english = input("enter your grade in English language (A, B, C, D, E or F): ").upper()
# mathematics = input("enter your grade in Mathematics (A, B, C, D, E or F): ").upper()
# other_subject = input("Do you have (As or Bs) in your three other subjects?\nYes or No: ").lower()
# academic_qualification = (english == 'A' or english == 'B') and (mathematics == 'A' or mathematics == 'B') and (other_subject == 'yes')
# eligibility = (citizenship == "Yes") and (enrollment == "Yes") and (other_scholarships == "No") and (academic_qualification == True)
# print(f"Candidate Name: {name}\nAge: {age}\nCitizenship: {citizenship}\nEnrollment: {enrollment}\nAcademic Qualification: {academic_qualification}\nEligible: {eligibility}")

citizenzhip = input("Are you a citizen of Nigeria?\nYes or No: ").title()
if citizenzhip == "Yes":
    enrollment = input("Are you registered as a full-time undergraduate student in a recognized nigerian university?\nYes or No: ").title()
    if enrollment == "Yes":
        other_scholarship = input("Are you receiving any other scholarship from an entity in the Oil and Gas industry, whether national or internaltional?\nYes or No: ").title()
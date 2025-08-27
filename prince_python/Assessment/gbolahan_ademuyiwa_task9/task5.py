# Federal Government Scholarship Key Eligibility Requirements
# Collecting Users Details
citizenzhip = input("Are you a citizen of Nigeria?\nYes or No: ").title()
enrollment = input("Are you registered as a full-time undergraduate student in a recognized nigerian university?\nYes or No: ").title()
other_scholarship = input("Are you receiving any other scholarship from an entity in the Oil and Gas industry, whether national or internaltional?\nYes or No: ").title()
english = input("Enter your grade in English: ").upper()
mathematics = input("Enter your grade in Mathematics: ").upper()
other_subject = other_subject = input("Do you have (As or Bs) in your three other subjects?\nYes or No: ").title()
# Checking Users Eligibiity
if citizenzhip == "Yes":
    if enrollment == "Yes":
        if other_scholarship == "No":
            print('good')
            if english == "A" or "B":
                if mathematics == "A" or "B":
                    if other_subject == "Yes":
                        print("You are qualified for the Scholarship.")
                    else:
                        print("You didn't meet our requirement.\nThank you for participating in the scholarship.")
                else:
                    print("You didn't meet our requirement.\nThank you for participating in the scholarship.")
            else:
                print("You didn't meet our requirement.\nThank you for participating in the scholarship.")
        else:
            print("You didn't meet our requirement.\nThank you for participating in the scholarship.")
    else:
        print("You didn't meet our requirement.\nThank you for participating in the scholarship.")
else:
    print("You didn't meet our Requirement.\nThank you for participating in the scholarship.")
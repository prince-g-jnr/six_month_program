# Addmission Process
candidate_name = input("Enter your Name: ")
utme_score = int(input("Enter your UTME Score: "))
university_choice = input("Did you choose UNILAG as your first choice\nYes or No: ").title()
olevel_result = input("Do you have five(5) credit passes at one sitting in relevan o'level subjects, including English and Mathematics\nYes or No: ").title()
# Checking Candidate Eligibility
eligibility = (utme_score>=200) and (university_choice == "Yes") and (olevel_result == "Yes")
print(f"Name: {candidate_name}\nUTME Score: {utme_score}\nUniversity Choice: {university_choice}\nO'Level Result: {olevel_result}\nEligible: {eligibility}")
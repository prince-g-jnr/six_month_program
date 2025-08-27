# Creating an empty dictionary
# Creating a dictionary
student = {}
name = input("Enter your Name: ").title()
age = int(input("Enter your Age: "))
# storing name and age in a dictionary
student["name"] = name
student["age"] = age
# storing scores in a dictionary
scores = [70, 85, 90]
student["scores"] = scores
# Calculating average
average_score = sum(scores)/len(scores)
passed = average_score >= 50
student["passed"] = passed
# Checking if a student is a teenager
teenager = (age >= 13) and (age <= 19)
print(f"Student Record: \nName: {student["name"]} \nScores: {scores} \nAge: {student["age"]} \nPassed: {student["passed"]} \nTeenager: {teenager}")
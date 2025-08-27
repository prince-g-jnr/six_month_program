# Student Bio Data Data Storage
student = {}
# collecting student data
name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
gender = input("Enter your Gender: ")
courses = input("Enter your Courses: ").split()
student["name"] = name
student["age"] = age
student["gender"] = gender
student["course"] = courses
print("\tStudent Biodata")
print(f"Name\t\t{student.get("name")}\nAge\t\t{student["age"]}\nGender\t\t{student["gender"]}\nCourses\t\t{",".join(student["course"])}")
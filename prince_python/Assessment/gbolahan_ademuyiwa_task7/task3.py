# Days and Activities Pairing
days_of_the_week = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
print("Select any specific days of the weeks using 1-7: ")
specific_days = [days_of_the_week[int(input("Enter the first day: "))-1], days_of_the_week[int(input("Enter the sencond day: "))-1], days_of_the_week[int(input("Enter the third day: "))-1]]
print(specific_days)
activities = [input(f"Enter your activity on {specific_days[0]}: "), input(f"Enter your activity on {specific_days[1]}: "), input(f"Enter your activity on {specific_days[-1]}: ")]
print(specific_days)
days_and_activiteis = {day: activity for day, activity in zip(specific_days, activities)}
print(days_and_activiteis)
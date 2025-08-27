num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"{num1} == {num2} : {num1 == num2}")
# Explanation
# if the number the user enter in num1 and num2 are the same then the output is going to be true. 
# if the number the user enter in num1 and num2 are not the same the output is going to be false
print(f"{num1} != {num2} : {num1 != num2}")
# Explanation
# if the number the user enter in num1 and num2 are the same then the output is going to be false. 
# if the number the user enter in num1 and num2 are not the same the output is going to be true
print(f"{num1} > {num2} : {num1 > num2}")
# Explanation
# if the number the user enter in num1 is less than or equal to num2 the output is going to be false
# if the number the user enter in num1 is greater than num2 then the output is true
print(f"{num1} < {num2} : {num1 < num2}")
# Explanation
# # if the number the user enter in num1 is greater than or equal to num2 then the output is false
# if the number the user enter in num1 is less than num2 the output is going to be true

# # 3 Usecases
# "To know if the number of votes are similar to voters"
# "To confirm the number absentee in a class"
# "To check the amount of club playing in Premier League and Bundesliga"

premier_League = 20
bundesliga = 18
print(f"{premier_League} == {bundesliga} : {premier_League == bundesliga}")
# Output: False
print(f"{premier_League} != {bundesliga} : {premier_League != bundesliga}")
# Output:  True
print(f"{premier_League} > {bundesliga} : {premier_League > bundesliga}")
# Output: True
print(f"{premier_League} < {bundesliga} : {premier_League < bundesliga}")
# Output: False
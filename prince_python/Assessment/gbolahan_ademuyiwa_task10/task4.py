# Electricity Bill Formatter
try:
    customer_full_name = input("Enter your Full Name: ").title()
    units_consumed = int(input("Enter the Unit Consumed: "))
    cost_per_unit = float(input("Enter the Cost per Unit: "))
    total_bills = units_consumed * cost_per_unit
    print(f"Customer Full Name: {customer_full_name}\nUnits Consumed: {units_consumed}\nCost Per Unit: {cost_per_unit}\nTotal bills: {total_bills}" )
except ValueError:
    print("Error: Invalid Input")
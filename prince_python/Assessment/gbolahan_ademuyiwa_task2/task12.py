# Stimulated USSD Menu Interaction
print("Hello, Welcome to GT Bank")
ussd_code = input("Enter your USSD Code \"737\": ")
print("1. Buy Airtime\n2. Buy Data\n3. Transfer Airtime")
option = int(input("choose an option between 1-3: "))
print(f"You select option {option}")
amount = int(input("Enter your Amount: "))
print("Transaction Successful")
# Stimulated USSD Menu Interaction
# Designing a mock USSD interface
# Asking user to "dail" a USSD Code
# Printing a menu with at least 3 options
# Asking user to choose an option
# Using f-string and/or concatenation to display a confirmation mesage showing the selected option
# Asking for an amount (if applicable)
# Displaying a final message summarizing the transaction.
print("Hello, Welcome to GT Bank")
ussd_code = ""
while ussd_code != "*737#":
    ussd_code = input("Enter ussd code \"*737#\": ")
balance = 10000
while True:
    print("\n Menu:")
    print("1. Check Balance")
    print("2. Buy Airtime")
    print("3. Transfer Money")
    print("4. But Data")
    print("5. Withdraw")
    print("6. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        print(f"Your balance is: {balance}")
        break
    elif choice == "2":
        amount = int(input("Enter the amount of Airtime you want to buy: "))
        if amount <= balance:
            balance -= amount
            print(f"Your Airtime recharge of {amount} is successful. \nNew balance: {balance}")
            break
        else:
            print("Insufficient funds.")
    elif choice == "3":
        amount = int(input("Enter the amount you want to transfer: "))
        if amount <= balance:
            balance -= amount
            print(f"Your transfer of {amount} is successful. \nNew Balance: {balance}")
            break
        else:
            print("Insufficient funds.")
    elif choice == "4":
        amount = int(input("Enter the amount of Data you want to buy: "))
        if amount <= balance:
            balance -= amount
            print(f"Your data of {amount} is successful. \nNew balance: {balance}")
            break
        else:
            print("Insufficient funds.")
    elif choice == "5":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Your withdraw of {amount} is successful. \nNew balance: {balance}")
            break
    elif choice == "6":
        print("Thank you for Banking with us. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
# CURRENCY COVERTED
# Collect Input Data
amount_in_naira = float(input("Enter your Amount: "))
exchange_rate_in_us_dollar = float(input("Enter Exchange rate in US Dollar: "))
exchange_rate_in_pounds = float(input("Enter Exchange rate in British Pounds: "))

# currency coverter
usd_amount = amount_in_naira / exchange_rate_in_us_dollar
pounds_amount = amount_in_naira / exchange_rate_in_pounds

# Print Formatted Table
print(f"currency\t\t\tSymbol\tAmount\n-----------------------------------------------------\nAmount in Naira\t\t\t₦\t{amount_in_naira:,.2f}\nExchange rate to US Dollar\t$\t{usd_amount:,.2f}\nExchange to British Pounds\t£\t{pounds_amount:,.2f}")
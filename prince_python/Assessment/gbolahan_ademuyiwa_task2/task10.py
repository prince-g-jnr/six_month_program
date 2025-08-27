# School Fees Breakdown
school_name = input("Enter your School Name: ")
tution_fee = float(input("Enter your Tution Fee: "))
hostel_fee = float(input("Enter your Hostel Fee: "))
feeding_fee = float(input("Enter your Feeding Fee: "))
total = tution_fee + hostel_fee + feeding_fee

# school fee breakdown output
print(f"School Name: {school_name}\nTuition Fee: #{tution_fee:,}\nHostel Fee: #{hostel_fee:,}\nFeeding Fee: #{tution_fee:,}\nTotal: #{total:,}")
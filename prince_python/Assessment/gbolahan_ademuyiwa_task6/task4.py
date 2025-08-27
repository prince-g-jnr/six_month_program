# Create a Unique Voters Registration System
# Ask for voter names and store in a set
# If a voters tries to register twice, display a warning
# After registration, display the total number of unique voters

voters_names = {input("Enter your voters name: "), input("Enter your voters Name: "), input("Enter your voters Name: "), input("Enter your voters Name: "), input("Enter your voters Name: ")}
if len(voters_names) <5:
    print("Warning: some names are duplicates and will not be added")
print("Total Unique Voters after registration:", len(voters_names))
print("Unique Voters:", sorted(voters_names))
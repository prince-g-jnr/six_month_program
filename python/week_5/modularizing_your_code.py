# # Modularizing Your Code 3(Object Oriented PRogramming)
# # Class

# class Student:
#     def __init__(self, name, course, level):
#         print("Creating a new student...")
#         self.name = name
#         self.course = course
#         self.level = level
#         print(f"Student {name} has been created")

# # When you create a student, __init__ runs automatically
# kemi = Student("Kemi Adebayo", "Computer Science", 300)


# # How init and self work Together

# class NigerianStudent:
#     def __init__(self, name, state, course):
#         print(f"Step 1: Creating Student Object...")
#         self.name = name
#         self.state_of_origin = state
#         self.course = course
#         self.student_id = self.generate_id()
#         print(f"Step 6: {self.name} from {self.state_of_origin} is ready!")

#     def generate_id(self):
#         import random
#         return f"UNISAIL{random.randint(1000, 9999)}"

# # When you create an object, here's what happens:
# ayo = NigerianStudent("Ayo Daniel", "Lagos", "Street Statistics")
# print(ayo.name)
# print(ayo.student_id)

# # More Example
# class Phoneuser:
#     def __init__(self, name, network):
#         self.name = name
#         self.network = network
#         self.airtime = 0
#         print(f"{self.name} joined {self.network} network")

#     def buy_airtime(self, amount):
#         self.airtime += amount
#         return f"{self.name} now has ₦{self.airtime} airtime"
    
# # Creating multiple users
# abeeb = Phoneuser("Abeeb Bakare", "MTN")
# onisemo = Phoneuser("Onisemo Williams", "Airtel")

# # Each Person's actions affect only their own account
# print(abeeb.buy_airtime(500))
# print(onisemo.buy_airtime(1000))
# print(abeeb.airtime)
# print(onisemo.airtime)

# # Attributes
# # Defining Attributes of a student
# class Student:
#     def __init__(self, name, course, level, state_of_origin):
#         self.name = name
#         self.course = course
#         self.level = level
#         self.state_of_origin = state_of_origin
#         self.cgpa = 0.0

#     def get_cgpa(self, agrregate):
#         self.cgpa += agrregate
#         return f"{self.name} CGPA is {self.cgpa}"
    
# # Creating a student object
# Fathia = Student("Fathia Abdul", "Biochemistry", 300, "Ogun State")

# # Accessing attributes
# print(Fathia.name)
# print(Fathia.course)
# print(Fathia.state_of_origin)
# print(Fathia.get_cgpa(3.40))

# # # Types of Attributes
# # # 1. Instance Attributes - Unique to each object
# # Student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun")
# # Student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")

# # print(Student1.name)
# # print(Student2.name)

# # 2. Class Attributes-Shared by all objects of the

# class Student:
#     university = "FUTA"

#     def __init__(self, name, sport):
#         self.name = name
#         self.sport = sport

# student1 = Student("Nicolas Jackson", "Football")
# student2 = Student("Reece James", "Football")

# print(student1.name)
# print(student1.university)
# print(student1.sport)
# print(student2.name)
# print(student2.university)
# print(student2.sport)

# # Methods: The Actions (What Objeccts CAN DO)

# class Student:
#     def __init__(self, name, course, level):
#         # Attributes
#         self.name = name
#         self.course = course
#         self.level = level
#         self.cgpa = 0.0
#         self.fees_paid = False

#     #  Method: action the student can do
#     def pay_school_fees(self):
#         self.fees_paid = True
#         return f"{self.name} has paid school fees for {self.level} level"
    
#     # Method: another action
#     def register_courses(self):
#         if self.fees_paid:
#             return f"{self.name} has registered courses for {self.course}"
#         else:
#             return f"{self.name} must pay school fees first!"
    
#     # Method: calculate CGPA
#     def calculate_cgpa(self, grades):
#         if grades:
#             self.cgpa = sum(grades) / len(grades)
#             return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
#         else:
#             return "No grades provided"
        
# # Using method
# Abiodun = Student("Abiodun Akinola", "Gistology", 600)
# print(Abiodun.pay_school_fees())
# print(Abiodun.register_courses())
# print(Abiodun.calculate_cgpa([4.2, 3.8, 4.0, 3.5]))

# # Types of Methods

# # 1. Instance Methods - Work with specific object data
# # 'self' refers to the specific student
# def pay_school_fees(self):
#     return f"{self.name} has paid school fees"

# # 2. Class Methods - work with class-level data
# @classmethod
# def get_university(cls):
#     return cls.university

# # 3. Static Methods - Don't need object or class data
# @staticmethod
# def academic_calender():
#     return "Academic session runs from september to july"

# # How Attributes and Methods work Together
# # - Attributes store the data
# # - Methods use and modify that data

class BankAccount:
    def __init__(self, owner, bank_name, balance = 0):
        # ATTRIBUTES - What the accound HAS
        self.owner = owner
        self.bank_name= bank_name
        self.balance = balance
        self.account_number = self.generate_account_number()

# METHODS - What the account can DO
    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount
            return f"₦{amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: ₦{self.balance:,}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        """Remove money from the account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"₦{amount:,} withdrawn from {self.owner}'s account. New balance: ₦{self.balance:,}"
    
    def transfer(self, amount, recipient):
        """Transfer money to another account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"₦{amount:,} transferred from {self.owner} to {recipient}. Remaining balance: balance ₦{self.balance:,}"
        return "Transfer failed: Insufficient funds"
    
    def check_balance(self):
        """Check current balance"""
        return f"{self.owner}'s {self.bank_name} account balance: ₦{self.balance:,}"
    
    def generate_account_number(self):
        """Generate a unique account number"""
        import random
        return f"01{random.randint(10000000, 99999999)}"
    
# Creating and using the account
adunni_acount = BankAccount("Adunni Olaleye", "AXT Bank", 50000)

# Attributes (Characteristics)
print(f"owner: {adunni_acount.owner}")
print(f"Bank: {adunni_acount.bank_name}")
print(f"Account Number: {adunni_acount.account_number}")

# Methods (actions)
print(adunni_acount.deposit(25000))
print(adunni_acount.withdraw(10000))
print(adunni_acount.transfer(15000, "Sunday James"))
print(adunni_acount.check_balance())
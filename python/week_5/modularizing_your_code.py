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

# Atttibutes vs Methods
# Given this class, identify the attributes and methods

class NaijaPhone:
    def __init__(self, brand, model, network_provider):
        self.brand = brand
        self.model = model
        self.network_provider = network_provider
        self.airtime_balance = 0
        self.data_balance = 0
        self.is_on = False

    def power_on(self):
        self.is_on = True
        return f"{self.brand} phone is now on. Network: {self.network_provider}"
    
    def buy_airtime(self, amount):
        self.airtime_balance += amount
        return f"₦{amount} airtime purchased. Balance: ₦{self.airtime_balance}"
    
    def make_call(self, number):
        if self.is_on and self.airtime_balance > 0:
            self.airtime_balance -= 10
            return f"Calling {number}... Remaining airtime: ₦{self.airtime_balance}"
    
    def send_sms(self, message, number):
        if self.airtime_balance >= 4:
            self.airtime_balance -= 4
            return f"SMS sent to {number}: '{message}'. Remaining airtime: ₦{self.airtime_balance}"
        return "Insufficient airtime to send SMS"
    
# Creating the user details
emmanuel_phone = NaijaPhone("Xiaomi", "Redmi", "MTN")

# Attribues (characteristics)
print(emmanuel_phone.brand)
print(emmanuel_phone.model)
print(emmanuel_phone.network_provider)
    
# Method (actions)
print(emmanuel_phone.power_on())
print(emmanuel_phone.buy_airtime(500))
print(emmanuel_phone.make_call(+2347061265068))
print(emmanuel_phone.send_sms(+2347081265068, "Mr chris"))

    
# Given this class, identity the attributes and methods

class BRTBus:
    def __init__(self, route, bus_number):
        self.route = route
        self.bus_number = bus_number
        self.current_stop = "Ikorodu"
        self.passenger_count = 0
        self.fare = 300

    def announce_stop(self):
        return f"Next stop: {self.current_stop}. Fare is ₦{self.fare}"
    
    def board_passenger(self, count):
        self.passenger_count += count
        return f"{count} passenger boared. Total: {self.passenger_count}"
    
# creating drivers details
mr_duada = BRTBus("Oshodi", "EPE-123ZE")

# Attributes (Characteristics)
print(mr_duada.route)
print(mr_duada.bus_number)

# Method (action)
print(mr_duada.announce_stop())
print(mr_duada.board_passenger(50))

# Given this class, identity the attributes and methods

class MarketTrader:
    def __init__(self, name, market_name, goods):
        self.name = name
        self.market_name = market_name
        self.goods = goods
        self.daily_sales = 0

    def advertise_good(self):
        return f"{self.name} at {self.market_name}: Fresh {', '.join(self.goods)} available!"
    
    def make_sale(self, amount):
        self.daily_sales += amount
        return f"Sale made! Today's total: ₦{self.daily_sales}"
    
# Creating Marketers Details
mama_t = MarketTrader("Mama T", "Ijoko Market", ["Soft Drinks", "Event Rental"])

# Attributes (Characteristics)
print(mama_t.name)
print(mama_t.market_name)
print(mama_t.goods)

# Methods (action)
print(mama_t.advertise_good())
print(mama_t.make_sale(5000))

# Encapsulation
class NigerianBankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance
        self.__pin = "1234"
        self._transaction_history = []

    # Public methods - anyone can use these
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._transaction_history.append(f"Deposited ₦{amount:,}")
            return f"₦{amount:,} deposited successfully"
        return "Invalid deposit amount"
    
    def withdraw(self, amount, pin):
        if self.__verify_pin(pin):
            if amount <= self.balance:
                self.balance -= amount
                self._transaction_history.append(f"withdrew ₦{amount:,}")
                return f"₦{amount:,} withdrawn successfully"
            return "Insufficient funds"
        return "Invalid PIN"
    
    def check_balance(self, pin):
        if self.__verify_pin(pin):
            return f"Current Balance: ₦{self.balance:,}"
        return "Invalid PIN"
    
    # Private method - only the class can use this
    def __verify_pin(self, entered_pin):
        return entered_pin == self.__pin
    
    # Protected method - subclasses can use this
    def _get_transaction_history(self):
        return self._transaction_history.copy()

# Using the encapsulated account
ibrahim_account = NigerianBankAccount("Ibrahim Konate", 50000)

# These work - public interface
print(ibrahim_account.deposit(10000))
print(ibrahim_account.check_balance("1234"))
print(ibrahim_account.withdraw(5000, "1234"))
print(ibrahim_account.check_balance("1234"))

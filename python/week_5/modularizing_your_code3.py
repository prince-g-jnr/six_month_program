# Modularizing Your Code 3(Object Oriented PRogramming)
# Class

class Student:
    def __init__(self, name, course, level):
        print("Creating a new student...")
        self.name = name
        self.course = course
        self.level = level
        print(f"Student {name} has been created")

# When you create a student, __init__ runs automatically
kemi = Student("Kemi Adebayo", "Computer Science", 300)


# How init and self work Together

class NigerianStudent:
    def __init__(self, name, state, course):
        print(f"Step 1: Creating Student Object...")
        self.name = name
        self.state_of_origin = state
        self.course = course
        self.student_id = self.generate_id()
        print(f"Step 6: {self.name} from {self.state_of_origin} is ready!")

    def generate_id(self):
        import random
        return f"UNISAIL{random.randint(1000, 9999)}"

# When you create an object, here's what happens:
ayo = NigerianStudent("Ayo Daniel", "Lagos", "Street Statistics")
print(ayo.name)
print(ayo.student_id)

# More Example
class Phoneuser:
    def __init__(self, name, network):
        self.name = name
        self.network = network
        self.airtime = 0
        print(f"{self.name} joined {self.network} network")

    def buy_airtime(self, amount):
        self.airtime += amount
        return f"{self.name} now has ₦{self.airtime} airtime"
    
# Creating multiple users
abeeb = Phoneuser("Abeeb Bakare", "MTN")
onisemo = Phoneuser("Onisemo Williams", "Airtel")

# Each Person's actions affect only their own account
print(abeeb.buy_airtime(500))
print(onisemo.buy_airtime(1000))
print(abeeb.airtime)
print(onisemo.airtime)

# Attributes
# Defining Attributes of a student
class Student:
    def __init__(self, name, course, level, state_of_origin):
        self.name = name
        self.course = course
        self.level = level
        self.state_of_origin = state_of_origin
        self.cgpa = 0.0

    def get_cgpa(self, agrregate):
        self.cgpa += agrregate
        return f"{self.name} CGPA is {self.cgpa}"
    
# Creating a student object
Fathia = Student("Fathia Abdul", "Biochemistry", 300, "Ogun State")

# Accessing attributes
print(Fathia.name)
print(Fathia.course)
print(Fathia.state_of_origin)
print(Fathia.get_cgpa(3.40))

# # Types of Attributes
# # 1. Instance Attributes - Unique to each object
# Student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun")
# Student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")

# print(Student1.name)
# print(Student2.name)

# 2. Class Attributes-Shared by all objects of the

class Student:
    university = "FUTA"

    def __init__(self, name, sport):
        self.name = name
        self.sport = sport

student1 = Student("Nicolas Jackson", "Football")
student2 = Student("Reece James", "Football")

print(student1.name)
print(student1.university)
print(student1.sport)
print(student2.name)
print(student2.university)
print(student2.sport)

# Methods: The Actions (What Objeccts CAN DO)

class Student:
    def __init__(self, name, course, level):
        # Attributes
        self.name = name
        self.course = course
        self.level = level
        self.cgpa = 0.0
        self.fees_paid = False

    #  Method: action the student can do
    def pay_school_fees(self):
        self.fees_paid = True
        return f"{self.name} has paid school fees for {self.level} level"
    
    # Method: another action
    def register_courses(self):
        if self.fees_paid:
            return f"{self.name} has registered courses for {self.course}"
        else:
            return f"{self.name} must pay school fees first!"
    
    # Method: calculate CGPA
    def calculate_cgpa(self, grades):
        if grades:
            self.cgpa = sum(grades) / len(grades)
            return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
        else:
            return "No grades provided"
        
# Using method
Abiodun = Student("Abiodun Akinola", "Gistology", 600)
print(Abiodun.pay_school_fees())
print(Abiodun.register_courses())
print(Abiodun.calculate_cgpa([4.2, 3.8, 4.0, 3.5]))

# Types of Methods

# 1. Instance Methods - Work with specific object data
# 'self' refers to the specific student
def pay_school_fees(self):
    return f"{self.name} has paid school fees"

# 2. Class Methods - work with class-level data
@classmethod
def get_university(cls):
    return cls.university

# 3. Static Methods - Don't need object or class data
@staticmethod
def academic_calender():
    return "Academic session runs from september to july"

# How Attributes and Methods work Together
# - Attributes store the data
# - Methods use and modify that data

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

# Absraction

from abc import ABC, abstractmethod

# Abstract base class - defines what a Nigerian studen should do
class NigerianStudent(ABC):
    def __init__(self, name, course, level):
        self.name = name
        self.course = course
        self.level = level
        self.fees_paid = False

    # concrete method - all students can do this
    def pay_school_fees(self, amount):
        self.fees_paid = True
        return f"{self.name} paid ₦{amount:,} school fees"
    
    # Abstract method - each type of student implements differently
    @abstractmethod
    def study_method(self):
        pass

    @abstractmethod
    def take_exam(self):
        pass

# Concrete classes - specific implementations
class MedicalStudent(NigerianStudent):
    def study_method(self):
        return f"{self.name} studies anatomy books and practices on cadavers"
    
    def take_exam(self):
        return f"{self.name} takes practical exam in the anatomy lab"
    
class EngineeringStudent(NigerianStudent):
    def study_method(self):
        return f"{self.name} solves mathematical problem and builds prototypes"

    def take_exam(self):
        return f"{self.name} takes exam with calculations and technical drawings"

class ComputerSciencesStudent(NigerianStudent):
    def study_method(self):
        return f"{self.name} codes programs and debugs software"

    def take_exam(self):
        return f"{self.name} takes pratical programming exam on computer"

# Using absraction
students = [
    MedicalStudent("Dr.Adeyinka Ogunsanya", "Medicine", 400),
    EngineeringStudent("Dr Ajala Gift", "Mechanical Engineering", 300),
    ComputerSciencesStudent("Fatima Hassan", "Computer Science", 200)
]

# Same interface, different implementations
for student in students:
    print(student.pay_school_fees(150000))
    print(student.study_method())
    print(student.take_exam())
    print("---")

# Simple abstraction for phone interface

class SimplePhone:
    def __init__(self, brand):
        self.brand = brand
        self._complex_internal_system = "Very complicated stuff"

    # Simple interface - user dosen't need to know internal complexity
    def make_call(self, number):
        self._establish_network_connection()
        self._encode_voice_signal()
        self._transmit_to_tower()
        return f"Callind {number} from {self.brand} phone..."
    
    def send_sms(self, message, number):
        self._connect_to_sms_center()
        self._format_message()
        self._send_through_network()
        return f"SMS sent to {number}: '{message}'"
    
    # Complex internal methods - hidden from user
    def _establish_network_connection(self):
        # complex networking code here
        pass

    def _encode_voice_signal(self):
        # complex audio processing here
        pass

    def _transmit_to_tower(self):
        # Complex radio transmission here
        pass

# User only needs to know the simple interface
my_phone = SimplePhone("Tecno")
print(my_phone.make_call(")8012345678"))
print(my_phone.send_sms("How far?" "08098765432"))

# Inheritance - Build on What Already Exists

"""
Inheritance allows you to create new classes based on existing ones. The new class (child) inherits attributes and methods from the parent class, and can add its own features or modify existing ones.
"""

# Parent class - Base Nigerian Person
class NigerianPerson:
    def __init__(self, first_name, last_name, state_of_origin):
        self.first_name = first_name
        self.last_name = last_name
        self.state_of_origin = state_of_origin
        self.can_speak_english = True

    def introduce(self):
        return f"My name is {self.first_name} {self.last_name} from {self.state_of_origin}"
    
    def greet(self):
        return "Good morning!"
    
    def speak_local_language(self):
        return "I speak my local language"

# child class 1 - Nigerian Student inherits from NigerianPerson
class NigerianStudent(NigerianPerson):
    def __init__(self, first_name, last_name, state_of_origin, course, level):
        # Inherit parent's initialization
        super().__init__(first_name, last_name, state_of_origin)
        # Add student - specific attributes
        self.course = course
        self.level = level
        self.cgpa = 0.0

    # override parent method with student - specific version
    def introduce(self):
        parent_intro =  super().introduce()   # Get parent's introduction
        return f"{parent_intro}, I'm a {self.level} level {self.course} student"
    
    # Add student - specific methods
    def study(self):
        return f"{self.first_name} is studying {self.course}"
    
    def take_exam(self):
        return f"{self.first_name} is writing {self.course} exam"
    
# Child class 2 - Nigerian worker inherits from NigerianPerson
class NigerianWorker(NigerianPerson):
    def __init__(self, first_name, last_name, state_of_origin, job_title, company):
        super().__init__(first_name, last_name, state_of_origin)
        self.job_title = job_title
        self.company = company
        self.salary = 0
    
    def introduce(self):
        parent_intro = super().introduce()
        return f"{parent_intro}. I work as a {self.job_title} at {self.company}"
    
    def work(self):
        return f"{self.first_name} is working as a {self.job_title}"

    def receive_salary(self, amount):
        self.salary += amount
        return f"{self.first_name} received ₦{amount:,} salary"
 
# Child class 3 - Nigerian Teacher (inherits from Nigerianworker)
class NigerianTeacher(NigerianWorker):
    def __init__(self, first_name, last_name, state_of_origin, subject, school):
        super().__init__(first_name, last_name, state_of_origin, "Teacher", school)
        self.subject = subject
        self.students = []

    def introduce(self):
        return f"My name is {self.first_name} {self.last_name} from {self.state_of_origin}. I teach {self.subject} at {self.company}"
    
    def teach(self):
        return f"Teacher {self.first_name} is teaching {self.subject}"
    
    def grade_students(self):
        return f"Teacher {self.first_name} is grading {self.subject} assignments"
    
# Using inheritance
# Create different types of people
student = NigerianStudent("Kemi", "Adebayo", "Lagos State", "Computer Science", 300)
worker = NigerianWorker("Chinedu", "Okafor", "Anambra State", "Software Developer", "Sail Innovation Lab")
teacher = NigerianTeacher("Chris", "Ekwugum", "Lagos State", "Data Science", "Sail Innovation Lab")

# All inherit basic Nigerian person abilities
print("=== Basic Inherited Methods ===")
print(student.greet())
print(worker.speak_local_language())
print(teacher.greet())

print("\n=== Customized Introductions ===")
print(student.introduce())
print(worker.introduce())
print(teacher.introduce())

print("\n=== Specific Abilities ===")
print(student.study())
print(worker.work())
print(teacher.teach())

# Types of Inheritance
# 1. Single Inheritance - One parent
class Parent:
    pass

class Child(Parent):
    pass

# 2. Multiple Inheritance - Multiple parents
class Father:
    def father_trait(self):
        return "Strong"
    
class Mother:
    def mother_trait(self):
        return "Caring"
    
class Child(Father, Mother):    # Inherits from both parents
    pass

child = Child()
print(child.father_trait())
print(child.mother_trait())

# How All (Abstraction, Encapsulation, Inheritance) Work Together
# Abstraction - Define what all school members should do

from abc import ABC, abstractmethod

class SchoolMember(ABC):
    def __init__(self, name, id_number):
        self._name = name              # Encapsulation - Protected attribute
        self._id_number = id_number    # Encapsulation - protected attribute

    @abstractmethod
    def daily_activity(self):          # Abstraction - must be implemented
        pass

    def get_info(self):                # common method for all
        return f"Name: {self._name}, ID: {self._id_number}"
    
# Inheritance - Student inherits from schoolMember
class Student(SchoolMember):
    def __init__(self, name, id_number, class_level):
        super().__init__(name, id_number) # Inheritance
        self.__grades = []                # Encapsulation - private

    def daily_activity(self):             # Abstraction - Implementation          
        return f"{self._name} attends classes and studies"
    
    def add_grade(self, subject, score):  # Encapsulation - controlled access
        if 0 <= score <= 100:
            self.__grades.append({"subject": subject, "score": score})
            return f"Grade added: {subject} = {score}"
        return "Invalid grade"
    
    def get_average(self):                # Encapsulation - controlled access
        if self.__grades:
            total = sum(grade["score"] for grade in self.__grades)
            return total / len(self.__grades)
        return 0
    
# Inheritance - Teacher inherits from SchoolMember
class Teacher(SchoolMember):
    def __init__(self, name, id_number, subject):
        super().__init__(name, id_number)
        self.__subject = subject          # Encapsulation - private

    def daily_activity(self):
        return f"{self._name} taeches {self.__subject} and grades assignments"
    
# Using all three principles together
student = Student("Adunni Olaleye", "STU001", "SS2")
teacher = Teacher("Mr. Emeka NWosu", "TCH001", "Mathematics")

# Polymorphism - same methhod, differnt behavior
print(student.daily_activity())
print(teacher.daily_activity())

# Encapsulation - controlled access to data
print(student.add_grade("Mathematics", 85))
print(student.add_grade("English", 78))
print(f"Average: {student.get_average()}")
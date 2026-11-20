"""
==============================================================
 BioSkillz CodeStart — Python Foundations | Batch 01
 Task 01: Variables, Data Types, Input, Operators & Typecasting
==============================================================

 Name     : Maheen Fatima

 Save as  : yourname_task_01.py   (example: ali_task_01.py)
 Deadline : Friday, 20 November 2026, 9:00 PM (PKT)
 Submit   : Upload this file to YOUR OWN GitHub repository.

 Empowering Skills | Lead with Science
"""


# ==============================================================
# PART A: SESSION EXERCISES
#
# The exercise questions are in the Session 01 recording.
# Session 01 recording (YouTube playlist): https://youtube.com/playlist?list=PLOMPeCDSq-kc&si=uY9I27bFj8yUqc00
# ==============================================================

# --------------------------------------------------------------
# Exercise 1: predict the output
# --------------------------------------------------------------

# My predictions (written before running):
#   1. print(7 / 2)             -> 3.5        (/ is true division, gives a float)
#   2. print(7 // 2)            -> 3          (// is floor division)
#   3. print("7" + "2")        -> 72         (+ joins two strings)
#   4. print(type(7.0))         -> <class 'float'>
#   5. print(2 + 3 * 4 ** 2)    -> 50         (** first: 16, then * : 48, then + : 50)
#   6. print(bool("0"))         -> True       (any non-empty string is True)

# Running them to check:
print(7 / 2)
print(7 // 2)
print("7" + "2")
print(type(7.0))
print(2 + 3 * 4 ** 2)
print(bool("0"))



# --------------------------------------------------------------
# Exercise 2: find and fix the bugs
# --------------------------------------------------------------

# Original buggy code:
#   1  Name = input("Name: ")
#   2  print("Hello", name)
#   3
#   4  age = input("Age: ")
#   5  print("Next year:", age + 1)
#   6
#   7  print("Done)
#
# Bug 1: SyntaxError, line 7
#        The string "Done) is missing its closing quote.
#        (Python reads the whole file first, so it reports this
#        before running anything.)
#        Fix: print("Done")
#
# Bug 2: NameError, line 2
#        The variable was created as Name (capital N) but used as
#        name. Python is case-sensitive.
#        Fix: name = input("Name: ")
#
# Bug 3: TypeError, line 5
#        input() returns a string, and a string cannot be added to
#        an integer.
#        Fix: convert with int(): int(age) + 1

# Fixed code:
name = input("Name: ")
print("Hello", name)

age = input("Age: ")
print("Next year:", int(age) + 1)

print("Done")



# --------------------------------------------------------------
# Exercise 3: Bill splitter
# --------------------------------------------------------------

total_bill = int(input("Total bill: "))
friends = int(input("Number of friends: "))

each_pays = total_bill // friends      # whole rupees per person
left_over = total_bill % friends       # rupees remaining

print("Each pays:", each_pays)
print("Left over:", left_over)

# Bonus: exact share with / compared with //
exact_share = total_bill / friends
print("Exact share:", exact_share)
print("Whole-rupee share (//):", each_pays)
print("Difference:", exact_share - each_pays)



# ==============================================================
# PART B: TASKS
# ==============================================================

# --------------------------------------------------------------
# Task 1: Variables and Data Types
# --------------------------------------------------------------

# Four variables about myself
name = "Maheen Fatima"      # string
age = 22                    # integer (change to your real age)
height = 1.5748             # float, height in metres
is_student = True           # boolean

# type() tells us the data type of each variable
print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))


# --------------------------------------------------------------
# Task 2: Temperature Converter (Input and Typecasting)
# --------------------------------------------------------------

# input() always returns a string, so convert it to float
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("Fahrenheit:", fahrenheit)
print("Kelvin:", kelvin)


# --------------------------------------------------------------
# Task 3: Simple Calculator (Arithmetic Operators)
# --------------------------------------------------------------

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Power:", num1 ** num2)


# --------------------------------------------------------------
# Task 4: Savings Tracker (Assignment Operators)
# --------------------------------------------------------------

savings = 1000
print("Starting savings:", savings)

savings += 500      # gift
print("After gift:", savings)

savings -= 300      # books
print("After buying books:", savings)

savings *= 2        # doubling by year end
print("After doubling:", savings)


# --------------------------------------------------------------
# Task 5: Scholarship Check (Comparison and Logical Operators)
# --------------------------------------------------------------

marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))

marks_ok = marks >= 80
attendance_ok = attendance >= 75

print("Marks 80 or more:", marks_ok)
print("Attendance 75% or more:", attendance_ok)
print("Qualifies for scholarship:", marks_ok and attendance_ok)

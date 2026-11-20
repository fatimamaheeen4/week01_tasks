"""
==============================================================
 BioSkillz CodeStart — Python Foundations | Batch 01
 Task 02: Strings & Conditional Statements
==============================================================

 Name     : Maheen Fatima

 Save as  : yourname_task_02.py   (example: ali_task_02.py)
 Deadline : Friday, 20 November 2026, 9:00 PM (PKT)
 Submit   : Upload this file to YOUR OWN GitHub repository.

 Empowering Skills | Lead with Science
"""


# ==============================================================
# PART A: SESSION EXERCISES
#
# Session 02 recording (YouTube playlist): https://youtube.com/playlist?list=PLOMPeCDSq-kc&si=uY9I27bFj8yUqc00
# ==============================================================

# --------------------------------------------------------------
# Exercise 1: predict the output
# --------------------------------------------------------------

# My predictions (written before running):
#   1. print("Python"[1:4])          -> yth    (index 1 up to, not including, 4)
#   2. print("banana".count("an"))   -> 2      ("an" appears twice: b-an-an-a)
#   3. print("Hello"[-1])            -> o      (-1 is the last character)
#   4. print("Zebra" < "apple")      -> True   (uppercase letters come before
#                                               lowercase: "Z" = 90, "a" = 97)
#   5. print(5 > 3 and 2 > 4)        -> False  (True and False is False)
#   6. print(not "")                 -> True   (empty string is False, not flips it)

# Running them to check:
print("Python"[1:4])
print("banana".count("an"))
print("Hello"[-1])
print("Zebra" < "apple")
print(5 > 3 and 2 > 4)
print(not "")



# --------------------------------------------------------------
# Exercise 2: find and fix 4 bugs
# --------------------------------------------------------------

# Original buggy code:
#   1  marks = int(input("Marks: "))
#   2  if marks >= 50
#   3      print("Pass")
#   4  else:
#   5  print("Fail")
#   6
#   7  answer = input("Again? ")
#   8  if answer = "yes":
#   9      print("Restarting...")
#
# Bug 1: SyntaxError, line 2
#        The if statement is missing the colon at the end.
#        Fix: if marks >= 50:
#
# Bug 2: IndentationError, line 5
#        The code under else: must be indented.
#        Fix: indent print("Fail")
#
# Bug 3: SyntaxError, line 8
#        = assigns a value; == compares two values.
#        Fix: if answer == "yes":
#
# Bug 4 (bonus, no error message): logic bug, line 8
#        Comparison is case-sensitive, so "Yes" is not equal to
#        "yes" and nothing is printed when you type "Yes".
#        Fix: convert the answer to lowercase first with lower().

# Fixed code:
marks = int(input("Marks: "))
if marks >= 50:
    print("Pass")
else:
    print("Fail")

answer = input("Again? ")
if answer.lower() == "yes":
    print("Restarting...")



# --------------------------------------------------------------
# Exercise 3: Student Grader
# --------------------------------------------------------------

student_name = input("Student name: ").strip().title()   # clean the name
marks_text = input("Marks (0-100): ").strip()

# isdigit() checks that the input is a whole number
if marks_text.isdigit():
    student_marks = int(marks_text)

    if student_marks > 100:                      # bonus: marks above 100
        print("Marks must be 0–100")
    else:
        if student_marks >= 90:
            student_grade = "A"
        elif student_marks >= 80:
            student_grade = "B"
        elif student_marks >= 70:
            student_grade = "C"
        elif student_marks >= 50:
            student_grade = "D"
        else:
            student_grade = "F"

        print(f"{student_name} scored {student_marks}/100 → Grade {student_grade}")
else:
    print("Marks must be a number")



# ==============================================================
# PART B: TASKS
# ==============================================================

# --------------------------------------------------------------
# Task 1: Name Formatter (String Methods)
# --------------------------------------------------------------

full_name = input("Enter your full name: ")

print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Title case:", full_name.title())
print("Total characters:", len(full_name))
print("Number of 'a':", full_name.lower().count("a"))   # lower() so 'A' is counted too


# --------------------------------------------------------------
# Task 2: Email Breakdown (Indexing and Slicing)
# --------------------------------------------------------------

email = input("Enter your email: ")

at_position = email.find("@")      # save the position of @ first

print("First character:", email[0])
print("Last character:", email[-1])
print("Position of @:", at_position)
print("Username:", email[:at_position])
print("Domain:", email[at_position + 1:])
print("Gmail address:", email.endswith("@gmail.com"))


# --------------------------------------------------------------
# Task 3: Report Card (f-strings and Typecasting)
# --------------------------------------------------------------

report_name = input("Enter your name: ")
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

total = subject1 + subject2 + subject3
percentage = (total / 300) * 100

print("----- Report Card -----")
print(f"Name: {report_name}")
print(f"Total: {total} out of 300")
print(f"Percentage: {percentage:.2f}%")


# --------------------------------------------------------------
# Task 4: Grade Calculator (if, elif and else)
# --------------------------------------------------------------

grade_marks = int(input("Enter your marks: "))

# Check for invalid marks first
if grade_marks < 0 or grade_marks > 100:
    print("Invalid marks")
elif grade_marks >= 85:
    print("Grade: A")
elif grade_marks >= 70:
    print("Grade: B")
elif grade_marks >= 55:
    print("Grade: C")
elif grade_marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")


# --------------------------------------------------------------
# Task 5: Login Checker (Nested Conditions)
# --------------------------------------------------------------

username = input("Enter username: ").strip().lower()   # not case-sensitive
password = input("Enter password: ")                   # case-sensitive

if username == "codestart":
    if password == "python123":
        print("Login successful. Welcome to CodeStart!")
    else:
        print("Incorrect password. Please try again.")
else:
    print("Username not found.")



# ==============================================================
# Before you submit, check that:
#   [ ] Your name is written at the top of this file
#   [ ] The file is saved as yourname_task_02.py
#   [ ] The whole file runs without errors
#   [ ] Your output matches the examples
# ==============================================================

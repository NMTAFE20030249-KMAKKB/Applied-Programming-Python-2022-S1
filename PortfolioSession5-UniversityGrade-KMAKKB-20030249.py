##################################################################################
#
#  Portfolio Session 5 - University Grade
#
#  File:       Assessment/Portfolio/Session_5/PortfolioSession5-UniversityGrade
#              -KMAKKB-20030249.py
#  Project:    KMAKKB Programming Portfolio Part 1 - Session 5 - UniversityGrade
#  Author:     Ku Muhammad Adam Ku Kamal Bahrin (20030249@tafe.wa.edu.au)
#  Copyright:  © Copyright 2021, Ku Muhammad Adam Ku Kamal Bahrin
#
##################################################################################
#

# Getting user input for the assessment score  to be assessed
score = float(input("Give me assessment score that is to be evaluated: "))

# Input validation to make sure the user gives the program the right value
while(score < 0):
    print("ERROR: INCORRECT VALUE")
    score =  float(input("Please enter a value equal or greater than 0: "))

if score >= 90 and score <= 100:
    print("HIGH DISTINCTION")
elif score >= 80 and score <= 89:
    print ("DISTINCTION")
elif score >= 70 and score <= 79:
    print ("CREDIT")
elif score >= 50 and score <= 69:
    print ("PASS")
else:
    print("Hello World")

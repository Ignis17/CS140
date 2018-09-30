# Author: Joel Turbi
# Assignment: Homework Assignment #6.2
# Course: CS140

height = int(input("What is your height in inches?"))
weight = int(input("What is your weight in pounds?")) 
heightSquared = height **2
BMIinchespounds = weight / heightSquared
BMI = BMIinchespounds * 703
print("BMI:")
print(BMI)
if BMI <=18.5:
    print("You are considered underweight")
if (BMI >=18.5) and (BMI <=24.9):
    print("You are considered healthy")
if (BMI >=25) and (BMI <=29.9):
    print("You are considered overweight")
if BMI >30:
    print("You are considered obese")
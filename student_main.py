import student_result as s
from details import student_details
from cal_total import calculate_total
from cal_average import calculate_average
from get_result import get_result
from grade import show_grade

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))

student_details(name, roll_no)

total = calculate_total(m1, m2, m3)
print("Total Marks:", total)

average = calculate_average(total)
print("Average Marks:", average)

result = get_result(average)
print("Result:", result)

grade = s.show_grade(average)
print("Grade:", grade)
def student_details(name, roll_no):
    print("\nStudent Details")
    print("Name:", name)
    print("Roll No:", roll_no)


def calculate_total(m1, m2, m3):
    total = m1 + m2 + m3
    return total


def calculate_average(total):
    average = total / 3
    return average


def get_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


def show_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"
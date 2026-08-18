class student_profile:
    def __init__(self,name,id,course,email,skills):
        self.student_name=name
        self.id=id
        self.course=course
        self.email=email
        self.skills=skills

student1=student_profile("Mohan",101,"python","mohanprakash9390@gmail.com",["htmml","css"])
print(student1.student_name)
print(student1.id)
print(student1.course)
print(student1.email)
print(student1.skills)
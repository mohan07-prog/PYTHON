class Course:
    def __init__(self,name,duration,trainer_name,technologies,start_date):
        self.name=name
        self.duration=duration
        self.trainer_name=trainer_name
        self.technologies=technologies
        self.start_date=start_date
    def display_course(self):
        print("Course Name:",self.name, "Duration:", self.duration, "Trainer Name:", self.trainer_name, "Technologies:", self.technologies, "Start Date:", self.start_date)    
    def is_tech_covered(self,tech):
        if tech in self.technologies:
            return True
        else:
            return False

course1=Course("mohan","2 Months","Salman",["html","css","java"],"02-08-26")
course1.display_course()
res=course1.is_tech_covered("java")
print(res)

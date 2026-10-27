class Employee:

    CompanyName="KodNest" #class variable
    
    def __init__(self,id,name):     #id, name are local var
        self.id = id  #instance variable
        self.name = name #instance variable
    
    def printdetails(self):
        print(Employee.CompanyName) #class variable
        print(self.id) #instance variable
        print(self.name) #instance variable

e1= Employee(11 , "Mohan") #reference variable
print(e1.id)
print(e1.name)
print(Employee.CompanyName)
print()
e2 = Employee(12, "Hruday")
print(e2.id)
print(e2.name)
print(Employee.CompanyName)
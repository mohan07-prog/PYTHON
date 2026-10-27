class Student:
    def __init__(self,roll,name):
        if roll>0:
            self.__roll = roll
        else:
            self.__roll = None
            print("enter the correct number")
        self.__name = name

    @property
    def roll(self):
        return self.__roll
    @property
    def name(self):
        return self.__name
    @roll.setter
    def roll(self,roll):
        self.__roll = roll
    @name.setter
    def name(self,name):
        self.__name = name

s1 = Student(7, "Mohan")
print(s1.roll)
print(s1.name)
print("----------")
s1.roll=45
s1.name="Hruday"
print(s1.roll)
print(s1.name)
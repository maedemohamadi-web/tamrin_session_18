class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.brain=Brain()

    def walk(self):
        print("walk")

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"


class Nurse(Person):
     def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.salary = salary

     def help(self):
        print("help people")

     def walk(self):
        print("walk fastly")

     def __repr__(self):
         return f"Person(name={self.name}, age={self.age}, salary={self.salary})"

#nurse1 = HeadNurse("nurse1", 10, 20)
#nurse1.walk()
#nurse1.help()
#print(nurse1)

class Brain:
    def think(self):
        print("think")


#new_nurse = HeadNurse("narges", 30, 2000000)
#print (new_nurse.brain.think())

class Hospital:
    def __init__(self, name, address,head_nurse):
        self.name = name
        self.address = address
        self.head_nurse = head_nurse

    def __repr__(self):
        return f"Hospital({self.__dict__})"

head_nurse=Nurse("maral",40,100)
print(head_nurse)




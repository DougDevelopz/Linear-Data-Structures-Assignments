class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setName(self):
        self.name = self.name

    def getName(self):
        return self.name

    def setAge(self):
        self.age = self.age

    def getAge(self):
        if self.age < 0: print("Age must be positive!")
        return self.age

    def __str__(self):
        return "The pet's name is " + self.name + " and is " + str(self.age) + " years old"

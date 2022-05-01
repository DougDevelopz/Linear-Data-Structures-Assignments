from Pet import Pet


class Dog(Pet):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def setBreed(self):
        self.breed = self.breed

    def getBreed(self):
        return self.breed

    def __str__(self):
        return "My dog's name is " + self.name + " and he is a " + str(self.age) + " year old " + self.breed + "!"

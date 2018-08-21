class Human:
    """Represents Human being"""
    population = 0

    def __init__(self, name):
        self.name = name
        Human.population += 1

    def __del__(self):
        Human.population = Human.population - 1
        print("Decrementing the population")

    def sayHi(self):
        print("Hi, My name is %s" % self.name)

    def howMany(self):
        if Human.population == 1:
            print("I am the only one here")

        else:
            print("there are %d guys left" % Human.population)


per1 = Human("Rohan")
per1.sayHi()
per1.howMany()

per2 = Human("Rajesh")
per2.howMany()


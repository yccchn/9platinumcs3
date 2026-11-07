class Animal: # create parent class
    def __init__(self, name):
        self.__name = name # store the name

    def get_name(self):
        pass 

    def make_sound(self):
        pass

class Lion(Animal): # create child class Lion
    def __init__(self, name):
        super().__init__(name) # initialize parent attributes

    def make_sound(self): # overrides the make_sound method
        print(f"{self.name} roars loudly!") #prints that lion is roaring loudly
    def eat(self): # overrides the eat method
        print(f"{self.name} eats fresh meat.") #prints that lion is eating fresh meat

class Elephant(Animal): # create child class Elephant
    def __init__(self, name):
        super().__init__(name) # initialize parent attributes

    def make_sound(self): # overrides the make_sound method
        print(f"{self.name} trumpets!") #prints that elephant is trumpeting
    def eat(self): # overrides the eat method
        print(f"{self.name} eats grass and fruits.") #prints that elephant is eating grass and fruits

class Monkey(Animal): # create child class Monkey
    def __init__(self, name):
        super().__init__(name) # initialize parent attributes

    def make_sound(self): # overrides the make_sound method
        print(f"{self.name} chatters!") #prints that monkey is chattering
    def eat(self): # overrides the eat method
        print(f"{self.name} eats bananas and nuts.") #prints that monkey is eating bananas and nuts

    animals = [ # creates a list of all objects
        Lion("Simba"), # creates a Lion object
        Elephant("Dumbo"), # creates an Elephant object
        Monkey("George")] # creates a Monkey object

    for animal in animals: # loop through all animals in list
        animal.make_sound() # calls make_sound
        animal.eat() # calls eat
        print("-----")
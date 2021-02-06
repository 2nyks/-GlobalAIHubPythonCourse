class Animals():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Animal created.')

    def who_am_i(self):
        print('I am a animal.')

    def eat(self):
        print('I am eating.')

class Dogs(Animals):
    def __init__(self, fname, lname, specie):
        Animals.__init__(self, fname, lname)
        self.dogSpecie = specie
        print('Dog created.')

    def who_am_i(self):
        print('I am a dog.')

    def bark(self):
        print('Hello, I am barking.')

class Cats(Animals):
    def __init__(self, fname, lname, specie):
        Animals.__init__(self, fname, lname)
        self.catSpecie = specie
        print('Cat created.')

    def who_am_i(self):
        print('I am a cat.')

    def meow(self):
        print('Hello, I am meowing.')

a = Animals("Pamuk", "Özbek")
d = Dogs("Bobby", "Yılmaz", "Pit Bull")
c = Cats("Lena", "Kalkan", "British")

d.who_am_i()
c.meow()
d.bark()

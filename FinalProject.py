class Employee():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.language = set({})

    def Language(self,languageList):
        self.language.add(languageList)

    def ShowInfo(self):
        for i in self.language:
            print(i)


class Manager():
    def __init__(self, fname, lname, age, language):
        self.firstName = fname
        self.lastName = lname
        self.age = age
        self.language = language


e1 = Employee("Şevval", 21)
e1.Language("French")
e1.Language("English")
e2 = Employee("Hans", 22)
e2.Language("German")
e3 = Employee("Tom", 25)
e3.Language("Turkish")
e3.Language("English")
e4 = Employee("Monica", 27)
e4.Language("German")

employees = [e1, e2, e3, e4]
languages = []
for e in employees:
    languages.append(e.language)
print(languages)


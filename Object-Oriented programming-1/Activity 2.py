class student:
    grade=10
    name="Penguin"

    def indroduction(self):
        print("Hi I am a student.")

    def details(self):
        print("My name is", self.name)
        print("I study in grade", self.grade)


ob=student()
ob.indroduction()
ob.details()            
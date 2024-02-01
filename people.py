class Person:
    def __init__(self, name: str, age: int, money: float, discount: float = 1) -> None:
        self.name = name
        self.age = age
        self.money = money
        self.discount = discount

    def greet(self):
        print(f"Hi there! My name is {self.name} and I am {self.age} years old.")

    def purchase(self, amount: float):
        if self.money > amount:
            self.money -= amount
        else:
            print("Not enough funds!")

    def deposit(self, amount: float):
        self.money += amount

    def buyLunch(self, meal: str):
        if meal.lower() == "cheeseburger":
            self.purchase(3 * self.discount)
        elif meal.lower() == "mac and cheese":
            self.purchase(2.5 * self.discount)
        elif meal.lower() == "pancakes":
            self.purchase(5 * self.discount)
        else:
            print(
                "Not a valid meal choice! Choose:\nCheeseburger\nMac and Cheese\nPancakes"
            )

    def __repr__(self) -> str:
        # __repr__ is programmer use, think debugging/logging
        return f"Person object with name {self.name}, age {self.age}, and ${self.money} dollars"

    def __str__(self) -> str:
        # __str__ is user use, think printing
        return f"{self.name}, {self.age}"


class Student(Person):
    def __init__(self, name: str, age: int, money: float, grade: int) -> None:
        super().__init__(name, age, money)
        self.grade = grade
        self.grades = [100] * 8  # short hand to initalize a list of eight 100's
        self.knowledge: float = 50

    def greet(self):
        print(f"Hi there! My name is {self.name} and I am in grade {self.grade}")

    def changeGrade(self, classSlot: int, newGrade: int) -> None:
        # assume a list of 8 elements, 1 for each class of the day
        if classSlot < 0 or classSlot > 7:
            print("Invalid class slot")

        self.grades[classSlot] = newGrade

    def getLetterGrade(self, classSlot: int) -> None:
        if classSlot < 0 or classSlot > 7:
            print("Invalid class slot")

        if self.grades[classSlot] >= 90:
            print("A")

        if self.grades[classSlot] < 90 and self.grades[classSlot] >= 80:
            print("B")

        if self.grades[classSlot] < 80 and self.grades[classSlot] >= 70:
            print("C")

        if self.grades[classSlot] < 70 and self.grades[classSlot] >= 60:
            print("D")

        if self.grades[classSlot] < 60:
            print("F")


class Teacher(Person):
    def __init__(
        self,
        name: str,
        age: int,
        money: float,
        subject: str,
        rate: float,
        discount: float = 0.5,
    ) -> None:
        super().__init__(name, age, money, discount)
        self.subject = subject
        self.wage = 1_000  # you can use underscores in python as a way to make larger numbers easier to read
        self.rate = rate

    def getPay(self, time: int):
        # note that time is in days and wage in dollars
        self.money += time * self.wage

    def tutor(self, time: float, student: Student):
        # note that time is in hours here
        student.knowledge += 1.5 * time
        student.purchase(self.rate * time)
        self.deposit(self.rate * time)

    def greet(self):
        print(f"Hi my name is {self.name} and I teach {self.subject}")

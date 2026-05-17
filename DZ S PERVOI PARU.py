import random


class Student:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.knowledge = 50
        self.money = 100
        self.happiness = 50
        self.alive = True

    def study(self):
        print(" Студент навчається")
        self.knowledge += 10
        self.energy -= 15
        self.happiness -= 5
        self.money -= 5

    def work(self):
        print(" Студент працює")
        self.money += 50
        self.energy -= 20
        self.happiness -= 10

    def rest(self):
        print(" Студент відпочиває")
        self.energy += 20
        self.happiness += 15
        self.money -= 20

    def eat(self):
        print(" Студент їсть")
        self.energy += 10
        self.money -= 10

    def check_status(self):
        print(
            f"Енергія: {self.energy}, "
            f"Знання: {self.knowledge}, "
            f"Гроші: {self.money}, "
            f"Щастя: {self.happiness}"
        )

        # Перевірка стану
        if self.energy <= 0:
            print(" Студент перевтомився")
            self.alive = False

        if self.knowledge <= 0:
            print(" Студента відрахували")
            self.alive = False

        if self.happiness <= 0:
            print(" Студент впав у депресію")
            self.alive = False

        if self.money < -100:
            print(" Студент загруз у боргах")
            self.alive = False

    def live_one_day(self, day):
        print(f"\n===== День {day} =====")

        # Розумна поведінка
        if self.money < 20:
            self.work()

        elif self.knowledge < 40:
            self.study()

        elif self.energy < 30:
            self.rest()

        else:
            action = random.choice(
                [self.study, self.work, self.rest, self.eat]
            )
            action()

        # Пасивні зміни
        self.energy -= 5
        self.knowledge -= 1
        self.happiness -= 2

        self.check_status()


student = Student("Іван")

for day in range(1, 366):
    if not student.alive:
        break

    student.live_one_day(day)

if student.alive:
    print("\n Студент успішно прожив рік!")
else:
    print("\n Симуляція завершилась достроково.")
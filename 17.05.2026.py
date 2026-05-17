class Animal:
    def __init__(self , name , age ):
        self.name = name
        self.age = age

        self.health = 100


    def info(self):
        print("Ім'я:" , self.name)
        print("Вік:" , self.age)
        print("HP:" , self.health)

    def sound(self):
        print("Тварина видаэ звук")

class Cat(Animal):
    def __init__(self , name , age , speed):

        super().__init__(name , age)

        self.speed = speed

    def info(self):
        super().info()
        print("Швидкість" , self.speed)

    def sound(self):
        print("Кіт мяукає")

cat = Cat ("Барсик" , 3 , 50)
cat.sound()
cat.info()

class Dog(Animal):
    def __init__(self , name , age , speed):

        super().__init__(name , age)

        self.speed = speed

    def info(self):
        super().info()
        print("Швидкість" , self.speed)

    def sound(self):
        print("Собака гавка'є")

dog = Dog ("Шарик" , 8 , 40)
dog.sound()
dog.info()

class WildAmimal(Animal):
    def __init__(self , name , age , danger):

        super().__init__(name , age)

        self.danger = danger

    def attack(self):

        print(self.name, "Атакує")

class Lion(WildAmimal):

    def __init__(self , name , age , danger):

        super().__init__(name , age , danger)

        self.roar_power = 100

    def roar(self):

        print(self.name , "голосно ричить")

class Tiger(WildAmimal):

    def __init__(self , name , age , danger):

        super().__init__(name , age , danger)

        self.roar_power = 80

    def roar(self):

        print(self.name , "голосно ричить")

class Wolf(WildAmimal):

    def __init__(self , name , age , danger):

        super().__init__(name , age , danger)

        self.roar_power = 50

    def roar(self):

        print(self.name , "ричить")





print("Сила:" , cat.health)

animal = Animal("Барсик" , 3)
animal = Animal("Шарик" , 8)

animal.info()


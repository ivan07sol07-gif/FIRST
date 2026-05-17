class Weapon:
    def __init__(self, name , damage):
        self.name = name
        self.damage = damage

    def info(self):
        print("Ім'я:" ,self.name)
        print("Урон:" ,self.damage)




class Enemy:
    def __init__(self, name , helth):
        self.name = name
        self.helth = helth

    def info(self):
        print("Ворог:" ,self.name)
        print("HP ворога:" ,self.helth)


class Armor:
    def __init__(self, name , defense):
        self.name = name
        self.defens = defense


class Character:
    def __init__(self, name , level , weapon , armor):
        self.name = name
        self.level = level

        self.weapon = weapon
        self.armor = armor

        self.health = 100

    def info(self):
        print("Ім'я:" ,self.name)
        print("Рівень:" ,self.level)
        print(self.name,"використовує", self.weapon.name)

    def attack(self , enemy):
        print(self.name , "атакує" , enemy.name)

        enemy.helth = self.weapon.damage

        print(enemy.name , "отримав шкоду")
        print("HP ворога" , enemy.helth)

    def info(self):
        print("Ім'я:", self.name)
        print("HP:" ,self.health)
        print("Зброя:" , self.weapon.name)
        print("Броня:" , self.armor.name)
armor1 = Armor("Iron Armor", 15)

weapon1= Weapon("Steel Sword", 30)

player1 = Character("Ciri", 17, weapon1 , armor1)

weapon1= Weapon("Bow" , 10)
weapon2 = Weapon("Magic Staff" , 25)

weapon1.info()
weapon2.info()

player1 = Character("Ciri" , 17 ,weapon1 , armor1)
player2 = Character("Witcher" , 22, weapon2 ,  armor1)

GaunterODim = Enemy("GaunterODim" , 100)

player1.attack(GaunterODim)
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
    def __init__(self, name , level ):
        self.name = name
        self.level = level

        self.health = 100

    def info(self):
        print("Ім'я:" ,self.name)
        print("Рівень:" ,self.level)
        print("HP:", self.health)


class Mag(Character):

    def __init__(self, name , level , strength):

        super().__init__(name , level)

        self.strength = strength




class Witcher(Character):

    def __init__(self, name , level , WitcherSenses):

        super().__init__(name , level)

        self.WitcherSenses = WitcherSenses

Witcher = Witcher("Mag", 5 , 60)

Witcher.info()

print("Сила:" , Witcher.WitcherSenses)

Mag = Mag("Mag", 5 , 40)

Mag.info()

print("Сила:" , Mag.strength)
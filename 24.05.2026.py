class Hero:
    def __init__(self, name):
        self.name = name

        self.hp= 100
        self.mana = 50
        self.level = 1


    def attack(self):

        print(self.name , "атакує")

    def health(self):

        print(self.name, "лікуєтся")

class Mage(Hero):

    def acid_attack_(self, name):

        print(self.name ,"плюєтся кислотою")
m= Mage("Viper")
print (isinstance(m, Mage))
print (isinstance(m, Hero))

hero1 = Hero("Arthur")
hero2 = Hero("Genous")

print(dir(hero2))
print(dir(hero1))

print(type(hero1))
print(type(hero2))

if isinstance(hero1, Hero):
    print("це Hero")

if isinstance(hero2, Hero):
    print("це Hero")

hp = getattr(hero1, "hp")
print(hp)
hp = (getattr(hero2, "hp"))
print(hp)
hp = getattr(m, "hp")
print(hp)
mana = getattr(hero1, "mana")
print(mana)
mana = getattr(hero2, "mana")
print(mana)
mana = getattr(m, "mana")
print(mana)

print(m.level)

setattr(m, "level", 20)

print(m.level)

setattr(hero1, "inventory",[] )

hero1.inventory.append("Potion")
hero1.inventory.append("Bow")
hero1.inventory.append("Acid")

print(hero1.inventory)

if hasattr(hero1, "inventory"):

    print("У героя є інвентарь")

if hasattr(m , "inventory"):
    print("У героя є інвентарь")

delattr(hero1, "inventory")

print(hero1.__dict__)
print(hero2.__dict__)
print(m.__dict__)
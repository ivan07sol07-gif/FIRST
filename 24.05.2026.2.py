"""
x=int(input("Ведіть число:"))
print(10/x)

try:
    x=int(input("Ведіть число:"))

    res=(10/x)
except ZeroDivisionError:

    print("Не можна ділити на 0")

except ValueError:

    print("Треба водити число")

else:
   print(res)

finally:
    print("шили підрахунок")


try:
    age = int(input("Ведіть вік:"))

    if  age==0:
        raise ValueError("Не може бути 0")

    print("Ok")
except ValueError as e:
    print("Помилка" , e)
    """
class BamkAccount:
    def __init__(self,money):
        self.money=money

    def withdraw(self , amount):

        if amount < 0:
            raise ValueError("Не можна знімати мінус")
        if amount > self.money:
            raise ValueError("Недостатньо грошей")
        if amount == 0 :


account=BamkAccount(100)

try:
    take = int(input("Скільки зняти?:"))
    account.withdraw(take)

except ValueError as e:
    print("Помилка:", e)


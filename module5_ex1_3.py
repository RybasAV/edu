class Warrior:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.armor = 100
        self.endurance = 100

    def Coliseum(w2):
        print(f"{w2.name} проиграл")
        print(f"Сохранить жизнь {w2.name}? (Y/N)")
        res = input()
        if res.upper() == "Y":
            print(f"Вы спасли жизнь {w2.name}")
            w2.health == 0
        elif res.upper() == "N":
            print(f"{w2.name} был убит")
            w2.health == 0

    def attack(w1, w2):  # воин 1 атакует, воин 2 не защищается
        time.sleep(2)
        print(f"{w1.name} атаковал воина {w2.name}")

        if w2.armor > 0 and w1.endurance > 0:  # проверяем броню и выносливость
            w2.health -= 20  # отнимаем здоровье
        elif w2.armor <= 0 and w1.endurance > 0:  # проверяем броню и выносливость
            w2.health -= random.randint(1, 30)  # отнимаем здоровье
        elif w1.endurance == 0:
            w2.health -= random.randint(0, 10)  # отнимаем здоровье

        if w1.endurance != 0:
            w1.endurance -= 10  # отнимаем выносливость у атакующего
        if w2.health <= 10:
            Warrior.Coliseum(w2)
        else:
            print(f"У {w2.name} осталось {w2.health} здоровья")
            print()

    def attack_protect(w1, w2):  # воин 1 атакует, воин 2 защищается
        time.sleep(2)
        print(f"{w1.name} атакует {w2.name} защищается")

        if w2.armor > 0 and w1.endurance > 0:  # проверяем осталась ли броня
            w2.health -= random.randint(0, 10)  # отнимаем здоровье
            w2.armor -= random.randint(0, 10)
        elif w2.armor <= 0 and w1.endurance > 0:
            w2.health -= random.randint(1, 30)  # отнимаем здоровье
        elif w1.endurance == 0:
            w2.health -= random.randint(0, 10)  # отнимаем здоровье

        if w1.endurance != 0:
            w1.endurance -= 10  # отнимаем выносливость у атакующего
        if w2.health <= 10:
            Warrior.Coliseum(w2)
        else:
            print(f"У {w2.name} осталось {w2.health} здоровья")
            print()

    def attack_attack(w1, w2):  # воин 1 атакует, воин 2 атакует
        time.sleep(2)
        print(f"Воины атакуют друг друга")
        w2.health -= random.randint(10, 30)  # отнимаем здоровье
        w1.health -= random.randint(10, 30)  # отнимаем здоровье

        if w1.endurance != 0:
            w1.endurance -= 10
        if w2.endurance != 0:
            w2.endurance -= 10

        if w2.health <= 10:
            Warrior.Coliseum(w2)
        elif w1.health <= 10:
            Warrior.Coliseum(w2)

        else:
            print(f"У {w1.name} осталось {w1.health} здоровья")
            print(f"У {w2.name} осталось {w2.health} здоровья")
            print()

    def protect(w1, w2):
        print("Оба воина защищаются")
        print(f"У {w1.name} осталось {w1.health} здоровья")
        print(f"У {w2.name} осталось {w2.health} здоровья")
        print()


import random
import time

w1 = Warrior("Мастер клинка")
w2 = Warrior("Вождь минотавров")
while w1.health > 10 and w2.health > 10:
    n = random.randint(1, 6)
    if n == 1:
        Warrior.attack(w1, w2)
    elif n == 2:
        Warrior.attack(w2, w1)
    elif n == 3:
        Warrior.attack_protect(w1, w2)
    elif n == 4:
        Warrior.attack_protect(w2, w1)
    elif n == 5:
        Warrior.attack_attack(w2, w1)
    elif n == 6:
        Warrior.protect(w2, w1)

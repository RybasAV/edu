import json


class Warrior:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.armor = 100
        self.endurance = 100
        print(f"Создан объект {self.name}")

    def save(w1):
        dict_war = vars(w1)
        with open(f"{w1.name}.json", "w", encoding="utf-8") as f:
            json.dump(dict_war, f, ensure_ascii=False, indent=4)
        print(f"Значение атрибутов {w1.name} записаны в файл")


w = Warrior("Мастер клинка")
w1 = Warrior("Вождь минотавров")
Warrior.save(w1)
Warrior.save(w)

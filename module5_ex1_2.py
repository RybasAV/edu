class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        print(f"Создан объект {self.name} класса Point, с координатами x={x} y={y}")

    def what_quarter(self):
        if self.x > 0 and self.y > 0:
            print(f"точка {self.name} находится в I - четверти")
        elif self.x < 0 and self.y > 0:
            print(f"точка {self.name} находится во II - четверти")
        elif self.x < 0 and self.y < 0:
            print(f"точка {self.name} находится в III - четверти")
        elif self.x > 0 and self.y < 0:
            print(f"точка {self.name} находится в IV - четверти")

    def length_point(point1, point2):
        lenght = ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5
        print(f"Расстояние междну точками {point1.name} и {point2.name} ={lenght}")


a = Point("A", 3, 5)
a.what_quarter()
b = Point("B", -1, 2)
b.what_quarter()
Point.length_point(a, b)

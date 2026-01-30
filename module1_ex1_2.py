v = int(input('Введите скорость: '))
t = int(input('Введите время в пути:'))
if v * t < 109:
	print('Отметка: ', v*t)
else:
	print('Отметка: ', v*t%109)

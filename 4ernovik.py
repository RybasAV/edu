import random
from time import sleep
again = 'д'
while again.lower() == 'д':
    print('Бросаем кубики... ')
    sleep(0.5)
    print('Бросаем кубики.. ')
    sleep(0.5)
    print('Бросаем кубики. ')
    sleep(0.5)
    print('Бросаем кубики.. ')
    sleep(0.5)
    print('Бросаем кубики... ')
    sleep(0.5)
    print('Бросаем кубики.. ')
    sleep(0.5)
    print('Бросаем кубики. ')
    sleep(0.5)
    print('Значения граней:')
    print(random.randint(1, 6))
    print(random.randint(1, 6))
    again = input('Бросить кубики еще раз? (д = да, н = нет): ')
from random import randint, shuffle

doors = [1, 0, 0]  # 3 двери. 1 - приз, 0 - проигрыш
stubborn = 0  # счетчик выигрышей упертого игрока
unstable = 0  # счетчик выигрышей переменчивого игрока
for i in range(1000):
    shuffle(doors)  # перемешиваем массив doors
    f = randint(0, 2)  # генерируем выбор двери
    stubborn += doors[f]
    if doors[f] == 0:
        unstable += 1

print('Stubborn:', stubborn)
print('Unstable:', unstable)

from random import randint, shuffle

envelopes = [200, 100]  # 2 конверта с наличкой в 100 и 200 валюты
stubborn = 0  # счетчик выигрышей упертого игрока
unstable = 0  # счетчик выигрышей переменчивого игрока
for i in range(1000):
    shuffle(envelopes)  # перемешиваем конверты
    f = randint(0, 1)  # генерируем выбор конверта
    stubborn += envelopes[f]  # + упертому
    if f == 0:
        unstable += envelopes[1]  # +1 переменчивому
    else:
        unstable += envelopes[0]  # +1 переменчивому

print('Stubborn:', stubborn)
print('Unstable:', unstable)

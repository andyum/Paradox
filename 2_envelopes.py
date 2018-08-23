from random import randint, shuffle

envelopes = [200, 100]
stubborn = 0
unstable = 0
for i in range(1000):
    shuffle(envelopes)
    f = randint(0, 1)
    stubborn += envelopes[f]
    if f == 0:
        unstable += envelopes[1]
    else:
        unstable += envelopes[0]
print('Stubborn:', stubborn)
print('Unstable:', unstable)

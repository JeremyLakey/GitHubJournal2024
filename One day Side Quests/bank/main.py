import random

numberPlayers = 100
numGames = 10000
p = [0 for _ in range(numberPlayers)]
w = [0 for _ in range(numberPlayers)]

def toWin(t, cp):
    if t < 4:
        return True
    return False

def dumbRandom(t, cp):

    if t < 4:
        return True
    return roll() != 7

def risky(t, cp):

    if t < 8:
        return True
    return False

def balance(t, cp):
    if t < 6:
        return True
    return False

def safe(t, cp):
    if t < 4:
        return True
    return False


def roll():
    return random.randint(1, 6)

def think(t, cp):

    if t < 3:
        return True

    return t < cp + 3

r = 0
g = 0
while g < numGames:
    p = [0 for _ in range(numberPlayers)]
    r = 0
    print(g)
    while r < 20:
        t = 0
        pool = 0
        pIn = [True for _ in range(numberPlayers)]
        k = True
        while k:
            if True not in pIn:
                k = False
                continue

            for i in range(numberPlayers):
                if pIn[i]:
                    if not think(t, i):
                        pIn[i] = False
                    else:
                        p[i] += pool

            res = roll()
            res2 = roll()
            tot = res + res2
            if t < 3:
                if tot == 7:
                    pool += 70
                else:
                    pool += tot
            else:
                if tot == 7:
                    k = False
                elif res == res2:
                    pool *= 2
                else:
                    pool += tot

            t += 1

        r += 1
    m = 0
    mi = 0
    for i in range(numberPlayers):
        if m < p[i]:
            mi = i
            m = p[i]

    w[mi] += 1

    g += 1

for i in range(numberPlayers):
    w[i] /= numGames

mx = 0
mi = 0
for i in range(numberPlayers):
    if mx < w[i]:
        mx = w[i]
        mi = i
print(w)
print(mi)
print(w[mi])
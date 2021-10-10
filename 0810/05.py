import string
import random


def strgen(n):
    a = ''
    for i in range(n):
        a += (random.choice(string.ascii_letters))
    return a


def count(l):
    small = 0
    large = 0
    for i in l:
        if i in string.ascii_lowercase:
            small += 1
        elif i in string.ascii_uppercase:
            large += 1
    if large > small:
        return 1
    elif large < small:
        return -1
    else:
        return 0


def funct(list):
    num1 = 0
    num2 = 0
    for i in (list):
        y = count(i)
        if y == 1:
            num1 += 1
        elif y == 0:
            num2 += 1
    print('Больше заглавных букв:', num1 * 100 / len(list))
    print('Больше маленьких букв:', (len(list) - num1 - num2) * 100 / len(list))
    print('Одинаково:', num2 * 100 / len(list))


funct([strgen(1), strgen(2), strgen(3), strgen(4), strgen(5), strgen(6), strgen(7)])

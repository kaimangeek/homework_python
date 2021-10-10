def dateexam(d, m, y):
    '''
    Функция принимает дату и проверяет её на достоверность
    '''
    d_31 = [1, 3, 5, 7, 8, 10, 12]
    d_30 = [4, 6, 9, 11]
    if (y <= 2021) and (y > 0 and m > 0 and d > 0 and m < 13 and d < 32):
        if (y < 2021) or (y == 2021 and m < 10) or (y == 2021 and m == 10 and d <= 9):  # проверка на сегодняшнюю дату
            if d < 32 and m in d_31:
                return True
            elif d < 31 and m in d_30:
                return True
            elif m == 2:
                if (d == 29 and y % 4 == 0 and y % 100 != 0) or d < 29:
                    return True
    else:
        return False


help(dateexam)
print(dateexam(19, 5, 2003))

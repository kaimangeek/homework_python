def strsum(a, k):
    x = a
    for i in range(1, k + 1):
        x = x + int(str(a) * i)
    return x


print(strsum(2, 3))

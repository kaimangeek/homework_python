def find_stu(a, ball):
    for line in a:
        args = line.split()
        if len(args) != 3: continue
        name, surname = args[0], args[1]
        if args[2].isdigit():
            m = int(args[2])
            if m >= ball:
                print(name, '', surname)


way = input("Введите путь к файлу:")
ball = int(input("Введите проходной балл:"))
file = open(way, "r")
a = file.readlines()
find_stu(a, ball)
file.close()

def rigtname(name):
    return name[0].isupper() and name[1:].islower()


def namespisok():
    nameall = []
    name = ''
    while name != 'q':
        name = input()
        if rigtname(name):
            nameall.append(name)

    return nameall


print(namespisok())
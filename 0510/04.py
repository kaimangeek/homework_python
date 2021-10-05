def namespisok():
    nameall = []
    name = ''
    while name != 'q':
        name = input()
        if name != 'q':
            nameall.append(name)
        else:
            break
    return nameall


print(namespisok())

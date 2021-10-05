def change_name(name):
    namenew = []
    for i in range(len(name)):
        words_list = name[i].split()
        result = words_list[0] + ' ' + words_list[1][0] + '.' + words_list[2][0] + '.'
        namenew.append(result)
    return namenew

print(change_name(['Кайманов Дмитрий Игоревич',  'Бебра Аристарх Леопольдович']))
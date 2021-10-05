def change_name(name):
    words_list = name.split()
    result = words_list[0] + ' ' + words_list[1][0] + '.' + words_list[2][0] + '.'
    return result


print(change_name('Кайманов Дмитрий Игоревич'))

import random


def randomname(names, surnames, patronymics, num):
    result = []
    i = 0
    while i < num:
        name = random.choice(names)
        surname = random.choice(surnames)
        patronymic = random.choice(patronymics)
        new_name = name + ' ' + surname + ' ' + patronymic
        result.append(new_name)
        i = i + 1
    return result


print(randomname(['Дмитрий', 'Ангелина', 'Камиль', 'Александр', 'Сергей'], \
                 ['Кайманов', 'Лопес', 'Путин', 'Обама', 'Мотрикала'], \
                 ['Олегович', 'Владимирович', 'Дмитриевич', 'Игоревич', 'Артемович'], 3))
#yield
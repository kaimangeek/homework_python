import string


def clean_text(words_list):
    result = []
    for word in words_list:
        new_word = ''
        has_punctuation_mark = False
        for i in range(len(word)):
            if word[i] in string.punctuation:
                if i == len(word) - 1:
                    new_word = word[:i]
                elif i < len(word):
                    new_word = word[:i] + word[i + 1:]
                has_punctuation_mark = True

        if not has_punctuation_mark:
            new_word = word

        result.append(new_word.lower())
    return result


def count_words(words_list):
    set_words = set(words_list)
    words_dict = {word: words_list.count(word) for word in set_words}
    return words_dict


def top_10(words_dict):
    print('The top-10 words:')
    items = words_dict.items()
    items = sorted(items, key=lambda x: x[1], reverse=True)
    for word, counter in items[:10]:
        print(word, ': ', counter)


file = open("2.txt", "r")
s = file.read()
ct = clean_text(s.split())
top_10(count_words(ct))

def phonenumber():
    x = {}
    name = 0
    while name != "q":
        name = input()
        if name == "q":
            break
        number = input()
        if len(number) == 16:
            if number[0] == "+" and number[1].isdigit() and number[2] == "-" and number[6] == "-" \
                    and number[10] == "-" and number[13] == "-" and number[3:6].isdigit() \
                    and number[7:10].isdigit() and number[11:13].isdigit() and number[14:17]:
                x[name] = number
            else:
                print("Ошибка")
        else:
            print("Ошибка")
    print(x)


phonenumber()

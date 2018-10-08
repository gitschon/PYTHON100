
def level_1():
    from random import randint
    random_digit = randint(0, 100)
    print("Подсказка : " + str(random_digit))

    user_dig = int(input("Введите число от 0 до 100 : "))

    if user_dig == random_digit:
        print("Да это оно")
    else:
        if user_dig < random_digit:
            print("больше")
        else:
            print("меньше")
    print("Партия!!!")
    return

level_1()

def level_2():

    from random import randint

    game = True
    counter = 0
    while game:
        random_digit = randint(0, 100)
        print("Подсказка : " + str(random_digit))
        user_dig = int(input("Введите число от 0 до 100 : "))

        if user_dig == random_digit:
            print("Да это оно")
        else:
            if user_dig < random_digit:
                print("больше")
            else:
                print("меньше")
        counter += 1
        print("Партия!!! № : " + str(counter))
        des = str(input("Вы хотите продолжить игру Y/N :")).upper()
        if des == 'N':
            print("Игра завершена!!!")
            game = False
        elif des == "Y":
            print("Новая партия!!!")
            game = True
    return


level_2()


def level_3():

    from random import randint

    game = True
    counter = 0
    while game:
        counter += 1
        random_digit = randint(0, 100)
        print("Подсказка : " + str(random_digit))
        user_dig = int(input("Введите число от 0 до 100 : "))

        if user_dig == random_digit:
            print("Да это оно")
        else:
            if user_dig < random_digit:
                print("больше")
            else:
                print("меньше")

        if counter < 50:
            print("Партия!!! № : " + str(counter))
            des = str(input("Вы хотите продолжить игру Y/N :")).upper()
            if des == 'N':
                print("Игра завершена!!!")
                game = False
            elif des == "Y":
                print("Новая партия!!!")
                game = True
        else:
            print("Вы исчерпали лимит из " + str(counter) + " партий - игра завершена!!!!")
            game = False
    return


level_3()
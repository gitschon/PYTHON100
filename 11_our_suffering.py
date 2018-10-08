def mon_1(z, coins_number1, coin_type1, coins_number2, coin_type2):
    for i in range(coins_number1 + 1):
        for j in range(coins_number2 + 1):
            result = coin_type1 * i + coin_type2 * j
            if result == z:
                return (i, j)
            if result > z:
                return ("нельзя монетами выдать " + str(z))


print(mon_1(z=15, coins_number1=3, coin_type1=5, coins_number2=1, coin_type2=1))


def howdigits_2():
    x = str(input("Введите число :"))
    return len(x)

print(howdigits_2())


def ispolinom_3():
    ispol = str(input("Введите строку :"))
    if ispol == ispol[::-1]:
        return print("Полином")
    else:
        return print("Не полином")


ispolinom_3()

def replace_4(row_find, row_repl):
    row = str(input("Введите строку :"))
    return row.replace(row_find, row_repl)


print(replace_4("55", "66"))




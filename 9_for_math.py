def fib_1(n):
    fib_list = [1, 1]
    for i in range(len(fib_list), n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list


print(fib_1(20))


def fibN_2(n, ma):
    fib_list = [1 for i in range(n)]
    for i in range(len(fib_list),ma):
        sum = 0
        for j in range(1, 7):
            sum += fib_list[-j]
        fib_list.append(sum)
    return fib_list


print(fibN_2(7, 100))

def squaresdigi_3(n):
    return [x **2 for x in range(1, n+1, 2)]

print(squaresdigi_3(10))

def frame_4(a, b):
    for i in range(b):
        if i == 0 or i == b - 1:
            print("*" * a)
        else:
            print("*", " " * (a - 4), "*")
    return


frame_4(5, 5)

def sumpmult_5():
    a = int(input("Input a : "))
    b = int(input("Input b : "))
    sum = 0
    mult = 1
    for i in range(a, b+1):
        sum += i
        mult *= i
    return print('Сумма : ' + str(sum), 'Произведние : ' + str(mult))


sumpmult_5()



def evenodd_6():
    a = int(input("Input a : "))
    b = int(input("Input b : "))
    print([x for x in range(a, b+1) if x % 2 == 0])
    print([x for x in range(a, b+1) if x % 2 != 0])
    return


evenodd_6()

def negpolsort_7(list):
    print([x for x in list if x > 0])
    print([x for x in list if x < 0])
    return

negpolsort_7([-1, 2, -5, 4, 8])




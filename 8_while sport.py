def squareday_1(km):
    step = 0
    su = 0
    while su < km:
        step += 1
        su += 2 ** step

    return step


print(squareday_1(1000))
print(squareday_1(10000))


def simpledigday_2(km):
    sum_dist = 0
    days = 1
    num = 1
    while sum_dist < km:
        if_main = False
        while not if_main:
            num += 1
            if_main = True
            for i in range(2, days):
                if num % i == 0:
                    if_main = False
                    break
        sum_dist += num
        days += 1
    return days



print(simpledigday_2(1000))
print(simpledigday_2(10000))

def norm_15_3(d):
    km = 10
    day = 0
    while day < d:
        km += (km * 0.15)
        day += 1
    return km


print(norm_15_3(30))

def norm10_4_a(bkm):
    km = 10
    day = 0
    norm = 0
    while norm < bkm:
        day += 1
        norm = 10 + (km * 0.1)
        km += norm
    return day


print(norm10_4_a(20))


def norm10_4_b(sump):
    km = 10
    day = 0
    while km <= sump:
        km += (km * 0.1)
        day += 1

    return day


print(norm10_4_b(100))








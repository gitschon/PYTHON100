
def variant(s, n):
    count = (len(s) + len(n) % 5)
    return count


print(variant('foteev','viktor'))

n = variant('foteev','viktor')


def gentype_1(x):
    return [(i + 2)*2 for i in range(1, x)]


print(gentype_1(n))
list = gentype_1(n)


def doubletype_2(list):
    double_list = [i + 1 for i in list]
    return double_list


print(doubletype_2(list))
double_list = doubletype_2(list)

superlist = list + double_list

print(superlist)


def slice_3(li):
    lst = sorted(li, reverse=True)
    return lst[1:-1]


print(slice_3(superlist))


def threeslice_4(li):
    return [i for i in li if i % 3 == 1]


print(threeslice_4(superlist))



def anythree_5(li):
    count = int(len(li) / 3)
    return li[:count]

print(anythree_5(superlist))

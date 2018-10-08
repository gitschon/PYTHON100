def multstr_1():
    n = int(input("input digit n : "))
    strr = str(input("input str : "))
    return strr * n


print(multstr_1())


def stairyway_2():
    n = int(input("input N : "))
    for i in range(1, n+1):
        print("="*i)
    return


stairyway_2()

def lettercount_3():
    st = str(input("input string : "))
    for i in set(st.replace(" ", "")):
        print(i, st.count(i))
    return


lettercount_3()


def lettercount_slov_3():
    slov ={}
    st = str(input("input string : "))
    for i in set(st.replace(" ", "")):
        slov[i] = st.count(i)
    return slov

print(lettercount_slov_3())


def wordslong_4():
    st = str(input("input string : "))
    di = {}
    for i in st.split():
        ke = "длинной " + str(len(i))
        if ke in di.keys():
            di[ke] += 1
        else:
            di[ke] = 1
    return di

print(wordslong_4())



def countvir(x, y, z, f):
    return (f + (y + x)/y**z + (f * (z - f)/x) + (y - x) / x) / (-y + (f + y) / x ** z)


print(countvir(5, 2.3, 2, 7.8))
print(countvir(1234, 37872, 1231, 12314))



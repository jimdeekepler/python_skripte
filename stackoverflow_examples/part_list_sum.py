from timeit import timeit

def sum10(l):
    from itertools import accumulate
    return list(accumulate(reversed(l)))[::-1]+[l[0]]

def sum11(l):
    from itertools import accumulate
    return list(accumulate(l[::-1]))[::-1]+[l[0]]


def sum20(l):
    from numpy import cumsum
    return list(cumsum(l[::-1]))[::-1]+[l[0]]

def sum21(l):
    from numpy import cumsum
    return list(cumsum(reversed(l)))[::-1]+[l[0]]

l = list(range(1000000))
iter_0 = timeit(lambda: sum10(l), number=10)  #0.9411586019996321
iter_1 = timeit(lambda: sum11(l), number=10)  #1.0461340810015827
nump_0 = timeit(lambda: sum20(l), number=10)  #2.007877276000727
nump_1 = timeit(lambda: sum21(l), number=10)  #0.00016513599985046312
print(iter_0)
print(iter_1)
print(nump_0)
print(nump_1)

# from: https://stackoverflow.com/questions/56645826/get-the-corresponding-sums-of-parts-of-a-list


# and using itertools
def sum31(l):
    from itertools import accumulate
    return list(accumulate(reversed(l)))[::-1]

accu_1 = timeit(lambda: sum31(l), number=10)
print(accu_1)


import itertools
import timeit
from math import sqrt


def is_prime(a):
    if a < 2: return False
    sq = int(sqrt(a))
    for i in range(2, sq + 1):
        if a % i == 0:
            return False
    return True
    # return all(a % i for i in xrange(2, a))


def list_digits(a):
    n = len(str(a))
    ls = list(str(a)[0])
    for i in range(1, n):
        ls.append(str(a)[i])
    return ls


def sum_digits(ls):
    LEN = len(ls)
    sum = 0
    for i in range(LEN):
        sum += int(ls[i]) * 10 ** (LEN - i - 1)
    return sum


def list_circular(a):
    ll = [a]
    ls = list_digits(a)
    LEN = len(ls)
    for i in range(LEN - 1):
        ls.append(ls.pop(0))
        ll.append(sum_digits(ls))
    return ll


def list_permutations(a):
    ls = list(itertools.permutations(list_digits(a)))
    len1 = len(ls)
    ll = []
    for i in range(len1):
        ll.append(sum_digits(ls[i]))
    return ll


def check_list_prime(ll):
    # return all(is_prime(ll[i]) for i in xrange(len(ll)))
    for i in xrange(len(ll)):
        if is_prime(ll[i]) == False:
            return False
    return True


# print list_digits(5)
# print list_permutations(123)
print list_circular(197)
start = timeit.default_timer()
count = 0
for i in range(2, 1000000):
    if is_prime(i) == True and check_list_prime(list_circular(i)) == True:
        print i
        count += 1

print count
stop = timeit.default_timer()
print stop - start

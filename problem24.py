__author__ = 'sev_user'
import itertools
x = itertools.permutations('0123456789',9);
counter = 0
for i in x:
    counter += 1

    if counter == 1000000:
        print i
    else:
        pass
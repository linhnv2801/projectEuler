__author__ = 'sev_user'
N = 101
array = []
for x in range(2,101):
    for y in range(2,101):
        tmp = x**y
        if tmp not in array:
         array.append(tmp)
print len(array)

__author__ = 'sev_user'
x1 = 1
x2 = 1
x = x1 + x2
count = 0
while (len(str(x)) < 1001):
    count += 1
    x1 = x2
    x2 = x
    x = x1 + x2

print count-2
x = 0.0005
print "%.9f" % x
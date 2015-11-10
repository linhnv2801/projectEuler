def check(x):
    tmp = 0
    for i in str(x):
        tmp += int(i) ** 5
    if tmp == x:
        return "true"
    return "false"
sum = 0
for x in range(10000,355000):
    if check(x) == "true":
        sum += x
        print x

print sum
# 443839

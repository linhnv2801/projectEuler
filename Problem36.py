def checkPalindromic(num):
    s = str(num)
    len2 = len(s)
    mid = len2 / 2
    for i in range(0, mid):
        if s[i] != s[len2 - i - 1]:
            return "false"
    return "true"


def toBin(num):
    # return '{0:08b}'.format(num)
    return bin(num)[2:]


count = 0
for i in range(1000000):
    if checkPalindromic(i) == "true" and checkPalindromic(toBin(i)) == "true":
        count += i

print count

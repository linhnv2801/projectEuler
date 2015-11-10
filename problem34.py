def factorial(n):
    if n == 0 o n == 1:
        return 1
    mul = n
    for i in range(2,n):
        mul *= i
    return mul

#  9!*7 = 2540160
print factorial(0), " ", factorial(1)
total = 0
bound = 7 * factorial(9)
print bound
for i in range(10,bound):
    sum = 0
    for j in str(i):
        sum += factorial(int(j))
    if sum == i :
        print i
        total += i

print total

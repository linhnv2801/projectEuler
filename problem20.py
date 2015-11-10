__author__ = 'sev_user'
import math
# print math.factorial(100)
sum = 0
x = math.factorial(100)
for digit in str(x):
    sum += int(digit);

print sum
__author__ = 'sev_user'
N = 101
# print N
matrix = [[0 for x in range(N)] for x in range(N)]
#
# print matrix[0][0]
# print matrix[100][100]
matrix[N/2][N/2] = 1
x = 1
t = 1
for m in range(1,501):
	x = x + 4 * t + 10 * (2 * m)
	t = t + 4 * (2 * m)
print x
# print N/2
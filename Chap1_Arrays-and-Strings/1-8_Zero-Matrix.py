###############################################################################
#
# 1.8 Zero Matrix
# Write an algorithm such that if an element in a MxN matrix is 0, its entire
# row and column are set to 0.
#
###############################################################################

matrix = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 0],
    [1, 0, 3, 0, 5]
]


# O(MN)
def zero(matrix):
    M = len(matrix)
    N = len(matrix[0])

    zero_r = set()
    zero_c = set()

    for r in range(M):
        for c in range(N):
            if matrix[r][c] == 0:
                zero_r.add(r)
                zero_c.add(c)

    for r in zero_r:
        for col in range(N):
            matrix[r][col] = 0

    for c in zero_c:
        for row in range(M):
            matrix[row][c] = 0

    return matrix


for row in matrix:
    print row

print ""

for row in zero(matrix):
    print row

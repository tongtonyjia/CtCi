###############################################################################
#
# 1.7 Rotate Matrix
#
# Given an image reprented by an NxN matrix, where each pixel in the image is
# 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in
# place?
#
###############################################################################

"""
00 -> 04
01 -> 14
02 -> 24
03 -> 34
04 -> 44

10 -> 03
11 -> 13
12 -> 23
13 -> 33
14 -> 43
"""

matrix = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
]


def rotate_matrix_(matrix):
    N = len(matrix)
    new = list()

    for i in range(N):
        for j in range(N):
            if j == 0:
                new.append([matrix[j][N-1-i]])
            else:
                new[i].append(matrix[j][N-1-i])

    return new


def rotate_matrix(matrix):
    N = len(matrix)

    for layer in range(N/2):
        start = layer
        end = N-1-layer
        for i in range(start, end):
            offset = i - start
            top = matrix[start][i]
            matrix[start][i] = matrix[end-offset][start]
            matrix[end-offset][start] = matrix[end][end-offset]
            matrix[end][end-offset] = matrix[i][end]
            matrix[i][end] = top

    return matrix


for row in matrix:
    print row

print ""

new = rotate_matrix(matrix)
for row in new:
    print row

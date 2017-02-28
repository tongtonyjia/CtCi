###############################################################################
#
# 8.10 Paint Fill:
#
# Implement the "paint fill" function that one might see on many image editing
# programs. That is, given a screen (represented by a two-dimensional array of
# colors), a point, and a new color, fill in the surrounding area until the
# color changes from the original color.
#
###############################################################################

from copy import deepcopy


def _paint(screen, point, ori, new):
    row, col = point
    if row < 0 or row == len(screen) or col < 0 or col == len(screen[0]):
        return
    elif screen[row][col] != ori:
        return

    screen[row][col] = new
    _paint(screen, (row+1, col), ori, new)
    _paint(screen, (row-1, col), ori, new)
    _paint(screen, (row, col+1), ori, new)
    _paint(screen, (row, col-1), ori, new)


def paint(screen, point, new):
    row, col = point
    ori = screen[row][col]
    if ori == new:
        return screen

    _paint(screen, point, ori, new)

    return screen


screen = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 3],
    [0, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

for row in screen:
    print row

print ''

for row in paint(deepcopy(screen), (3, 4), 2):
    print row

print ''

for row in paint(deepcopy(screen), (0, 0), 2):
    print row

###############################################################################
#
# 8.12 Eight Queens:
#
# Write an algorithm to print all ways of arranging eight queens on an 8x8
# chess board so that none of them share the same row, column, or diagonal. In
# this case, "diagonal" means all diagonals, not just the two that bisect the
# board.
#
###############################################################################

from copy import deepcopy

SIZE = 5


def _check_valid(row, col, placements):
    for placement in placements:
        p_row, p_col = placement
        if col == p_col:
            return False
        if row - p_row == abs(col - p_col):
            return False

    return True


def _count_ways(row, placements, results):
    for col in range(SIZE):
        if _check_valid(row, col, placements):
            _placements = deepcopy(placements)
            _placements.append((row, col))
            if row == SIZE - 1:
                results.append(_placements)
                continue
            _count_ways(row+1, _placements, results)


def count_ways():
    placements = list()
    results = list()
    _count_ways(0, placements, results)

    return results


def _show_board(way):
    board = [[0 for row in range(SIZE)] for col in range(SIZE)]
    for row, col in way:
        board[row][col] = 8
    for row in board:
        print row
    print ''


ways = count_ways()
for way in ways:
    _show_board(way)

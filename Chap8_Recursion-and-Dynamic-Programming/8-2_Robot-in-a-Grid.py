###############################################################################
#
# 8.2 Robot in a Grid
#
# Imagine a robot sitting on the upper left corner of grid with r rows and c
# columns. The robot can only move in two directions, right and down, but
# certain cells are "off limits" such that the robot cannot step on them.
# Design an algorithm to find a path for the robot from the top left to the
# bottom right.
#
###############################################################################
from copy import deepcopy


maze = [
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0]
]


def get_path_r(maze, path):
    x, y = path[-1]

    if x == len(maze[0]) or y == len(maze):
        return None
    if x == len(maze[0])-1 and y == len(maze)-1:
        return path
    if maze[y][x] == 1:
        return None

    right_path = deepcopy(path)
    right_path.append((x+1, y))

    down_path = deepcopy(path)
    down_path.append((x, y+1))

    return (
        get_path_r(maze, right_path) or
        get_path_r(maze, down_path)
    )

path = list()
path.append((0, 0))
path = get_path_r(maze, path)
print path
maze_ = deepcopy(maze)
for x, y in path:
    maze_[y][x] = 8

print ''

for row in maze_:
    print row

print '\n\n\n'


def maze_map_d(maze):
    maze_map = [
        [[] for col in range(len(maze[0]))] for
        row in range(len(maze))
    ]
    maze_map[0][0].append([(0, 0)])
    for x in range(1, len(maze[0])):
        if maze[0][x] == 1:
            break
        maze_map[0][x] = deepcopy(maze_map[0][x-1])
        maze_map[0][x][0].append((x, 0))
    for y in range(1, len(maze)):
        if maze[y][0] == 1:
            break
        maze_map[y][0] = deepcopy(maze_map[y-1][0])
        maze_map[y][0][0].append((0, y))

    for x in range(1, len(maze[0])):
        for y in range(1, len(maze)):
            if maze[y][x] == 1:
                continue
            maze_map[y][x] = (
                deepcopy(maze_map[y-1][x]) + deepcopy(maze_map[y][x-1])
            )
            for path in maze_map[y][x]:
                path.append((x, y))

    return maze_map

maze_map = maze_map_d(maze)
for path in maze_map[-1][-1]:
    print path
    maze_ = deepcopy(maze)
    for x, y in path:
        maze_[y][x] = 8

    print ''

    for row in maze_:
        print row

    print '\n'

def is_valid(maze_size, _maze, x, y, res):
    """
    A utility function to check if x, y is valid index for N * N Maze
    """
    if x < 0 or y < 0 or x >= maze_size or y >= maze_size or _maze[x][y] != 1 or res[x][y] != 0:
        return False
    return True


def rat_in_maze(maze_size, _maze, move_x, move_y, x, y, res):
    """
    A recursive utility function to solve Maze problem
    """
    if x == maze_size - 1 and y == maze_size - 1:
        return True
    for i in range(4):
        x_new = x + move_x[i]
        y_new = y + move_y[i]

        if is_valid(maze_size, _maze, x_new, y_new, res):
            res[x_new][y_new] = 1
            if rat_in_maze(maze_size, _maze, move_x, move_y, x_new, y_new, res):
                return True
            res[x_new][y_new] = 0
    return False


def solve_maze(_maze):
    """
    Solve maz
    """
    res = [[0 for _ in range(MAZE_SIZE)] for _ in range(MAZE_SIZE)]
    res[0][0] = 1

    move_x = [-1, 1, 0, 0]
    move_y = [0, 0, -1, 1]

    if rat_in_maze(MAZE_SIZE, _maze, move_x, move_y, 0, 0, res):
        for i in range(MAZE_SIZE):
            for j in range(MAZE_SIZE):
                print(res[i][j], end=' ')
            print()
    else:
        print('Solution does  not exist')


if __name__ == "__main__":
    MAZE_SIZE = 4

    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]

    solve_maze(maze)

rat_maze = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 0, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0, 0, 1, 1]
]


def print_maze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            print(str(maze[i][j])+"\t",end="")
        print("\n")
    print("\n")


def safe(maze,x,y,sol):
    if x>=0 and y>=0 and x<len(maze) and y<len(maze[0]) and maze[x][y] == 1 and sol[x][y] != 1:
        return True
    return False


def solve(maze, x, y, sol):
    if (x == len(maze)-1) and y == (len(maze[0])-1):
        sol[x][y]=1
        return True

    if safe(maze,x,y,sol):
        sol[x][y]=1
        print_maze(sol)
        if solve(maze, x + 1, y, sol):
            return True
        if solve(maze, x, y + 1, sol):
            return True
        if solve(maze, x, y - 1, sol):
            return True
        if solve(maze, x - 1, y, sol):
            return True
        sol[x][y]=0
    return False

def solution(maze):
    sol = [[0 for j in range(len(maze[0]))] for i in range(len(maze))]
    if not solve(maze, 0, 0, sol):
        print("Solution does not exist.")
        return False
    print("----------------------------------------------\n")
    print_maze(rat_maze)
    print_maze(sol)
    return True


if __name__ == "__main__":
    solution(rat_maze)
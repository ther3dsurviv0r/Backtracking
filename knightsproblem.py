N=0
mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
mov_y = [1, 2, 2, 1, -1, -2, -2, -1]
def print_board(board):
    for i in range(N):
        for j in range(N):
            print(str(board[i][j])+"\t",end="")
        print("\n")


def safe(board,x,y):
    if x>=0 and y>=0 and x < N and y < N and board[x][y]==0:
        return True
    return False


def solution(board, x, y, step):
    if step > N ** 2:
        return True

    if safe(board,x,y):
        board[x][y] = step
        print(step)
        for i in range(8):
            if solution(board,x+mov_x[i],y+mov_y[i],step+1):
                return True
        board[x][y]=0
    return False


def solve():
    board = [[0 for i in range(N)] for j in range(N)]
    if not solution(board,0,0,1):
        print("No solution possible.")
    print("\n--------------------------\n")
    print_board(board)


if __name__ == "__main__":
    N = int(input("Enter the size of a square board: "))
    print("Please wait. It might take some time.")
    solve()

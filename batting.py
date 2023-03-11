import random
N = 5
board = []

def init():
    global board
    for i in range(N):
        board_1 = []
        for j in range(N):
            board_1.append(0)
        board.append(board_1)

def show_board():
    global board
    print("X",end=" ")
    for y in range(N):
        print(str(y),end=" ")
    print("y")
    for i in range(N):
        print(str(i),end=" ")
        for j in range(N):
            # アウト
            if board[i][j] == 0:
                if j == N-1:
                    print("x",)
                else:
                    print("x",end=" ")
            # 単打
            if board[i][j] == 1:
                if j == N-1:
                    print("①",)
                else:
                    print("①",end=" ")
            # 2塁打
            if board[i][j] == 2:
                if j == N-1:
                    print("②",)
                else:
                    print("②",end=" ")
            # 3塁打
            if board[i][j] == 3:
                if j == N-1:
                    print("③",)
                else:
                    print("③",end=" ")
            # 本塁打
            if board[i][j] == 4:
                if j == N-1:
                    print("●",)
                else:
                    print("●",end=" ")
    print("x")

def select_result(x,y):
    global board
    result = 0
    # 単打
    count = 0
    while count < N*N*0.3:
        rand_x = random.randrange(N)
        rand_y = random.randrange(N)
        if board[rand_x][rand_y] == 0:
            board[rand_x][rand_y] = 1
            count += 1
            if (x == rand_x) and (y == rand_y):
                result = 1
    # 2塁打
    count = 0
    while count < N*N*0.3*0.3:
        rand_x = random.randrange(N)
        rand_y = random.randrange(N)
        if board[rand_x][rand_y] == 1:
            board[rand_x][rand_y] = 2
            count += 1
            if (x == rand_x) and (y == rand_y):
                result = 2
    
    # 3塁打
    count = 0
    while count < N*N*0.3*0.1:
        rand_x = random.randrange(N)
        rand_y = random.randrange(N)
        if board[rand_x][rand_y] == 1:
            board[rand_x][rand_y] = 3
            count += 1
            if (x == rand_x) and (y == rand_y):
                result = 3

    # 本塁打
    count = 0
    while count < 1:
        rand_x = random.randrange(N)
        rand_y = random.randrange(N)
        if board[rand_x][rand_y] == 1:
            board[rand_x][rand_y] = 4
            count += 1
            if (x == rand_x) and (y == rand_y):
                result = 4
    
    return result

init()
show_board()
x = int(input("高さ:"))
y = int(input("コース:"))
result = select_result(x,y)
show_board()
print("結果:",end="")
if result == 0:
    print("アウト")
if result == 1:
    print("安打")
if result == 2:
    print("2塁打")
if result == 3:
    print("3塁打")
if result == 4:
    print("ホームラン!!!!!!!!")
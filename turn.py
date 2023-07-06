import globals

# move the tiles upward
def take_up_turn(board):
    [n,m] = [len(board),len(board[0])]
    merged = [[False for _ in range(n)] for _ in range(m)]

    for i in range(1,n):   # For i = 0, upward shifting is not possible
        for j in range(m):

            if board[i][j] == 0:    # Shifting will add no value
                continue

            shift = 0
            for k in range(i-1,-1,-1):
                if board[k][j] == 0:
                    shift += 1
                else:
                    break

            if shift > 0:
                board[i-shift][j] = board[i][j]
                board[i][j] = 0

            if i-shift-1 >= 0 and board[i-shift-1][j] == board[i-shift][j] and not merged[i-shift-1][j] and not merged[i-shift][j]:
                board[i-shift-1][j] *= 2
                globals.score += board[i-shift-1][j]
                board[i-shift][j] = 0
                merged[i-shift-1][j] = True

    return board


# move the tiles downward
def take_down_turn(board):
    [n,m] = [len(board),len(board[0])]
    merged = [[False for _ in range(n)] for _ in range(m)]

    for i in range(n-2,-1,-1):   # For i = n-1, downward shifting is not possible
        for j in range(m):

            if board[i][j] == 0:    # Shifting will add no value
                continue

            shift = 0
            for k in range(i+1,n):
                if board[k][j] == 0:
                    shift += 1
                else:
                    break

            if shift > 0:
                board[i+shift][j] = board[i][j]
                board[i][j] = 0

            if i+shift+1 < n and board[i+shift+1][j] == board[i+shift][j] and not merged[i+shift+1][j] and not merged[i+shift][j]:
                board[i+shift+1][j] *= 2
                globals.score += board[i+shift+1][j]
                board[i+shift][j] = 0
                merged[i+shift+1][j] = True

    return board


# move tiles rightward
def take_right_turn(board):
    [n,m] = [len(board),len(board[0])]
    merged = [[False for _ in range(n)] for _ in range(m)]

    for i in range(n):
        for j in range(m-2,-1,-1):   # For j = m-1, rightward shifting is not possible

            if board[i][j] == 0:    # Shifting will add no value
                continue

            shift = 0
            for k in range(j+1,m):
                if board[i][k] == 0:
                    shift += 1
                else:
                    break

            if shift > 0:
                board[i][j+shift] = board[i][j]
                board[i][j] = 0
            
            if j+shift+1 < m and board[i][j+shift+1] == board[i][j+shift] and not merged[i][j+shift+1] and not merged[i][j+shift]:
                board[i][j+shift+1] *= 2
                globals.score += board[i][j+shift+1]
                board[i][j+shift] = 0
                merged[i][j+shift+1] = True

    return board


# move tiles leftward
def take_left_turn(board,):
    [n,m] = [len(board),len(board[0])]
    merged = [[False for _ in range(n)] for _ in range(m)]

    for i in range(n):
        for j in range(1,m):    # For j = 0, leftward shifting is not possible

            if board[i][j] == 0:    # Shifting will add no value
                continue

            shift = 0
            for k in range(j-1,-1,-1):
                if board[i][k] == 0:
                    shift += 1
                else:
                    break

            if shift > 0:
                board[i][j-shift] = board[i][j]
                board[i][j] = 0

            if j-shift-1 >= 0 and board[i][j-shift-1] == board[i][j-shift] and not merged[i][j-shift-1] and not merged[i][j-shift]:
                board[i][j-shift-1] *= 2
                globals.score += board[i][j-shift-1]
                board[i][j-shift] = 0
                merged[i][j-shift-1] = True

    return board
def winCheck(board):
    for x in range(len(board)):
        for y in range(len(board[x])-3):
            a = board[x][y]
            if a==0:
                break
            if board[x][y+1] == a:
                if board[x][y+2] == a:
                    if board[x][y+3] == a:
                        if a==1:
                            return 1
                        elif a==2:
                            return 2
    for x in range(len(board)-3):
        for y in range(len(board[x])):
            a = board[x][y]
            if a==0:
                break
            if board[x+1][y] == a:
                if board[x+2][y] == a:
                    if board[x+3][y] == a:
                        if a==1:
                            return 1
                        elif a==2:
                            return 2
    for x in range(len(board)-3):
        for y in range(len(board[x])-3):
            a = board[x][y]
            if a==0:
                break
            if board[x+1][y+1] == a:
                if board[x+2][y+2] == a:
                    if board[x+3][y+3] == a:
                        if a==1:
                            return 1
                        elif a==2:
                            return 2
    for x in range(len(board)):
        for y in range(len(board[x])-3):
            a = board[x][y]
            if a==0:
                break
            if board[x-1][y+1] == a:
                if board[x-2][y+2] == a:
                    if board[x-3][y+3] == a:
                        if a==1:
                            return 1
                        elif a==2:
                            return 2
    return False
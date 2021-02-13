from CheckWin import *
from Move import *
from Text import *
while True:
    board = createBoard()
    while True:
        moveText(1)
        move(1,board)
        if(winCheck(board))==1:
            winText(1,0)
            break
        elif winCheck(board) == 2:
            winText(2,0)
            break
        moveText(2)
        move(2,board)
        if (winCheck(board)) == 1:
            winText(1,0)
            break
        elif winCheck(board) == 2:
            winText(2,0)
            break
from Board import *
from Speech import *
from CheckWin import *
from Text import *
movelist = []
pointlistx = []
pointlisty = []
keylist = ["q","w","e","r","t","y","u"]
numlist = ["0","1","2","3","4","5","6","7",0,1,2,3,4,5,6,7]
keymaps = {
    "q":1,
    "w":2,
    "e":3,
    "r":4,
    "t":5,
    "y":6,
    "u":7
}
def resetboard(board):
    movelist = []
    pointlistx = []
    pointlisty = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            board[x][y] = 0
    createBoard()

def move(player,board):
    while True:
        rawinput = listenforinput()
        mo = rawinput
        if rawinput == 'p':
            resetboard(board)
        if rawinput in keylist:
            templistx = []
            templisty = []
            num = keymaps.get(rawinput)
            col = board[num-1]
            for item in range(len(col)):
                templistx.append(num * 100 - 52)
                templisty.append((6- item) * 100 + 144)

            for item in range(len(templistx)):
                circ = Circle(Point(templistx[item],templisty[item]), 42)
                circ.setFill("white")
                circ.draw(win)
            circ = Circle(Point(templistx[item],144), 42)
            circ.setFill("white")
            circ.draw(win)
            del templistx[0]
            del templisty[0]
            del col[0]
            for item in range(len(templistx)):
                if col[item] == 1:
                    circ = Circle(Point(templistx[item], templisty[item]), 42)
                    circ.setFill("yellow")
                    circ.draw(win)
                if col[item] == 2:
                    circ = Circle(Point(templistx[item], templisty[item]), 42)
                    circ.setFill("red")
                    circ.draw(win)
            col.append(0)
            board[num-1] = col

            if (winCheck(board)) == 1:
                winText(1,1)
                break
            elif winCheck(board) == 2:
                winText(2,1)
                break
            break

        elif rawinput in numlist:
            mo = int(rawinput)
            if mo == 0:
                columnChange = movelist[-1]-1
                for x in range(len(board[columnChange])):
                    if board[columnChange][5-x] != 0:
                        board[columnChange][5-x] = 0
                        circ = Circle(Point(pointlistx[-1], pointlisty[-1]), 42)
                        circ.setFill("white")
                        circ.draw(win)
                        break
                del movelist[-1]
                del pointlistx[-1]
                del pointlisty[-1]
                board[7] = [0,0,0,0,0,0]
                board[8] = [0,0,0,0,0,0]
                break

            elif mo != 0:
                if board[mo - 1][-1] == 0:
                    movelist.append(mo)
                    if player==1:
                        for item in range(len(board[mo-1])):
                            if board[mo-1][item] == 0:
                                board[mo-1][item] = 1
                                circ = Circle(Point((mo * 100) - 52, (5-item) * 100 + 144), 42)
                                pointlistx.append(mo*100 -52)
                                pointlisty.append((5-item)*100+144)
                                circ.setFill("yellow")
                                circ.draw(win)
                                break
                    elif player==2:
                        for item in range(len(board[mo-1])):
                            if board[mo-1][item] == 0:
                                board[mo-1][item] = 2
                                circ = Circle(Point((mo * 100) - 52, (5-item) * 100 + 144), 42)
                                pointlistx.append(mo * 100 - 52)
                                pointlisty.append((5 - item) * 100 + 144)
                                circ.setFill("red")
                                circ.draw(win)
                                break
                    break
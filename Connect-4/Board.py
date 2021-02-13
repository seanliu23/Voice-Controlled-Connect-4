from graphics import *
txt = Text(Point(350, 50), 40)
win = GraphWin("Connect 4", 700, 700)
def createBoard():
    board =  [[0,0,0,0,0,0], [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    for item in win.items[:]:
        item.undraw()
    win.update()
    img = Image(Point (350,400), "connect_4_board.gif")
    img.draw(win)

    txt1 = Text(Point(46, 80), 40)
    txt1.setText("1")
    txt1.draw(win)
    txt2 = Text(Point(146, 80), 40)
    txt2.setText("2")
    txt2.draw(win)
    txt3 = Text(Point(246, 80), 40)
    txt3.setText("3")
    txt3.draw(win)
    txt4 = Text(Point(346, 80), 40)
    txt4.setText("4")
    txt4.draw(win)
    txt5 = Text(Point(446, 80), 40)
    txt5.setText("5")
    txt5.draw(win)
    txt6 = Text(Point(546, 80), 40)
    txt6.setText("6")
    txt6.draw(win)
    txt7 = Text(Point(646, 80), 40)
    txt7.setText("7")
    txt7.draw(win)

    return board

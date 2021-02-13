from Board import *

def moveText(player):
    if player == 1:
        txt.undraw()
        txt.setText("Player 1's Turn, Press A Key (1-7) To Move")
        txt.draw(win)
    if player == 2:
        txt.undraw()
        txt.setText("Player 2's Turn, Press A Key (1-7) To Move")
        txt.draw(win)
def winText(player, state):
    if player == 1:
        txt.undraw()
        txt.setText("Player 1 Wins!")
        txt.setTextColor('blue')
        txt.setSize(36)
        txt.draw(win)
        if state == 0:
            win.getKey()
    if player == 2:
        txt.undraw()
        txt.setText("Player 2 Wins!")
        txt.setTextColor('blue')
        txt.setSize(36)
        txt.draw(win)
        if state == 0:
            win.getKey()
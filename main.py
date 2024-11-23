from graphics import *

def main():
    win = Window(800, 600)
    cell_1 = Cell(200, 300, 400, 500, win)
    cell_2 = Cell(450, 550, 100, 200, win, top=False, left=False)
    cell_1.draw()
    cell_2.draw()
    win.wait_for_close()
    
main()
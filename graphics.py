from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
            
    def close(self):
        self.__running = False
        
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)
        
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
        )
        
class Cell:
    def __init__(self, x1, x2, y1, y2, win, right=True, left=True, top=True,
                 bottom=True):
        self.right = right
        self.left = left
        self.top = top
        self.bottom = bottom
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        
    def draw(self):
        if self.top:
            self._win.draw_line(Line(Point(self._x1, self._y2),
                                     Point(self._x2, self._y2)),
                                "black")
        if self.right:
            self._win.draw_line(Line(Point(self._x2, self._y2),
                                     Point(self._x2, self._y1)),
                                "black")
        if self.bottom:
            self._win.draw_line(Line(Point(self._x1, self._y1),
                                     Point(self._x2, self._y1)),
                                "black")
        if self.left:
            self._win.draw_line(Line(Point(self._x1, self._y1),
                                     Point(self._x1, self._y2)),
                                "black")    
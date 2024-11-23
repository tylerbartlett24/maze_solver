from graphics import Line, Point

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
            
    def draw_move(self, to_cell, undo=False):
        from_centre = Point((self._x1 + self._x2)/2, (self._y1 + self._y2)/2)
        to_centre = Point((to_cell._x1 + to_cell._x2)/2,
                          (to_cell._y1 + to_cell._y2)/2)    
        if undo:
            self._win.draw_line(Line(from_centre, to_centre), "gray")
        else:    
            self._win.draw_line(Line(from_centre, to_centre), "red")
    

from cell import Cell
import random
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        
    def _create_cells(self):
        self.maze = []
        
        for i in range(self._x1,
                       (self.num_cols + 1) * self.cell_size_x + self._x1,
                        self.cell_size_x
                       ):
            dimension = []
            for j in range(self._y1,
                           (self.num_rows + 1) * self.cell_size_y + self._y1,
                            self.cell_size_y
                            ):
                cell = Cell(i, 
                            i + self.cell_size_x,
                            j,
                            j + self.cell_size_y,
                            self._win,
                            )
                dimension.append(cell)
            self.maze.append(dimension)
            
        for x in self.maze:
            for y in x:
                y.draw()
                self._animate()
                
                
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
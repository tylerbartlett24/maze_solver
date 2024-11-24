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
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed is None:
            random.seed(0)
        else:
            random.seed(seed)
        self._create_cells()
        
    def _create_cells(self):
        self.maze = []
        
        for i in range(self._x1,
                        self.num_cols * self.cell_size_x + self._x1,
                        self.cell_size_x
                        ):
            dimension = []
            for j in range(self._y1,
                            self.num_rows * self.cell_size_y + self._y1,
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
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)
        
    def _break_entrance_and_exit(self):
        self.maze[0][0].top = False
        self.maze[0][0].draw()
        self.maze[-1][-1].bottom = False
        self.maze[-1][-1].draw()
        
        
    def whatever(self):
        random.seed()
        entrance_hole = random.randint(0, 1)
        exit_hole = random.randint(2, 3)
        match entrance_hole:
            
            case 0:
                self.maze[0][0].top = False
            case 1:
                self.maze[0][0].left = False
            case 2:
                self.maze[0][0].bottom = False
            case 3:
                self.maze[0][0].right = False
            case _:
                raise Exception("Trying to delete non-existent wall.")
        
        
        
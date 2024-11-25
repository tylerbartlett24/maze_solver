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
        time.sleep(0.02)
        
    def _break_entrance_and_exit(self):
        self.maze[0][0].top = False
        self.maze[0][0].draw()
        self.maze[-1][-1].bottom = False
        self.maze[-1][-1].draw()
        
        
    def break_walls_r(self, i, j):
        self.maze[i][j].visited = True
        while True:
            to_visit = []
            if i - 1 > 0:
                if self.maze[i - 1][j].visited == False:
                    to_visit.append("left")
            if i + 1 < self.num_cols:
                if self.maze[i + 1][j].visited == False:
                    to_visit.append("right")
            if j - 1 > 0:
                if self.maze[i][j - 1].visited == False:
                    to_visit.append("top")
            if j + 1 < self.num_rows:
                if self.maze[i][j + 1].visited == False:
                    to_visit.append("bottom")
            if len(to_visit) == 0:
                self.maze[i][j].draw()
                return
            direction = to_visit[random.randint(0, len(to_visit) - 1)]
            match direction:
            
                case "left":
                    self.maze[i - 1][j].right = False
                    self.maze[i][j].left = False
                    self.maze[i - 1][j].draw()
                    self.maze[i][j].draw()
                    self.break_walls_r(i - 1, j)
                case "right":
                    self.maze[i + 1][j].left = False
                    self.maze[i][j].right = False
                    self.maze[i + 1][j].draw()
                    self.maze[i][j].draw()
                    self.break_walls_r(i + 1, j)
                case "top":
                    self.maze[i][j - 1].bottom = False
                    self.maze[i][j].top = False
                    self.maze[i][j - 1].draw()
                    self.maze[i][j].draw()
                    self.break_walls_r(i, j - 1)
                case "bottom":
                    self.maze[i][j + 1].top = False
                    self.maze[i][j].bottom = False
                    self.maze[i][j + 1].draw()
                    self.maze[i][j].draw()
                    self.break_walls_r(i, j + 1)
                case _:
                    raise Exception("Trying to go in an illegal direction.")
                
    def _reset_visited(self):
        for i in self.maze:
            for j in i:
                j.visited = False
                
    def solve(self):
        self.solve_r(0, 0)
        
    def solve_r(self, i, j):
        self._animate()
        self.maze[i][j].visited = True
        if self.maze[i][j] == self.maze[-1][-1]:
            return True
        directions = ["left", "right", "bottom", "top"]
        for direction in directions:
            if direction == "left" and not self.maze[i][j].left:
                if not self.maze[i-1][j].visited:
                    self.maze[i][j].draw_move(self.maze[i-1][j])
                    if self.solve_r(i-1, j):
                        return True
                    else:
                        self.maze[i-1][j].draw_move(self.maze[i][j],undo=True)
            elif direction == "right" and not self.maze[i][j].right:
                if not self.maze[i+1][j].visited:
                    self.maze[i][j].draw_move(self.maze[i+1][j])
                    if self.solve_r(i+1, j):
                        return True
                    else:
                        self.maze[i+1][j].draw_move(self.maze[i][j],undo=True)
            elif direction == "top" and not self.maze[i][j].top:
                if not self.maze[i][j-1].visited:
                    self.maze[i][j].draw_move(self.maze[i][j-1])
                    if self.solve_r(i, j-1):
                        return True
                    else:
                        self.maze[i][j-1].draw_move(self.maze[i][j], undo=True)
            elif direction == "bottom" and not self.maze[i][j].bottom:
                if not self.maze[i][j+1].visited:
                    self.maze[i][j].draw_move(self.maze[i][j+1])
                    if self.solve_r(i, j+1):
                        return True
                    else:
                        self.maze[i][j+1].draw_move(self.maze[i][j], undo=True)
        return False
                    
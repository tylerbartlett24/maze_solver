import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.maze),
            num_cols,
        )
        self.assertEqual(
            len(m1.maze[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.maze),
            num_cols,
        )
        self.assertEqual(
            len(m1.maze[0]),
            num_rows,
        )
        
    def test_reset_visited(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1.break_walls_r(0, 0)
        m1._reset_visited()
        for i in m1.maze:
            for j in i:
                self.assertEqual(
                    j.visited,
                    False
                )


if __name__ == "__main__":
    unittest.main()
import unittest

from maze import Maze
''' 
class Maze:
  def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
'''

class Tests(unittest.TestCase):
  def test_maze_create_cells(self):
    num_cols = 12
    num_rows = 10
    m1 = Maze(0,0,num_rows, num_cols, 10,10)
    print(f"\nTesting maze creation with {num_cols} columns and {num_rows} rows.")
    self.assertEqual(
      len(m1._cells),
      num_cols,
    )
    self.assertEqual(
      len(m1._cells[0]),
      num_rows,
    )
  
  def test_maze_start_point(self):
    start_x = 5
    start_y = 5
    m1 = Maze(start_x, start_y, 5,5, 10, 10)
    print(f"\nTesting maze creation with maze starting at {start_x} pixels from left and {start_y} pixels from top.")
    self.assertEqual(m1._x1,start_x)
    self.assertEqual(m1._y1, start_y)

  def test_maze_entrance_exit_creation(self):
    num_cols = 5
    num_rows = 6
    m1 = Maze(0,0,num_rows,num_cols,10,10)

    print("\nTesting if the first and last cells have entrance and exit.")
    print(f"\tFirst cell Top Wall: {m1._cells[0][0].has_top_wall}")
    print(f"\tLast cell Top Wall: {m1._cells[num_cols-1][num_rows-1].has_top_wall}")
    self.assertEqual(m1._cells[0][0].has_top_wall, False)
    self.assertEqual(m1._cells[num_cols-1][num_rows-1].has_bottom_wall, False)

    # self.assertEqual(m1._cells[0])


if __name__ == "__main__":
  unittest.main()


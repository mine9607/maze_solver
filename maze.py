
from cells import Cell
import random
import time
class Maze:
  def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
    self._cells = []
    self._x1 = x1
    self._y1 = y1
    self._num_rows = num_rows
    self._num_cols = num_cols
    self._cell_size_x = cell_size_x
    self._cell_size_y = cell_size_y
    self._win = win
    self.seed = random.seed(seed)

    self._create_cells()
    self._break_entrance_and_exit()
  
  def _create_cells(self):
    '''  
    This function should fill a self.__cells list with lists of cells

    Each top-level list is a column of Cell Objects.

    Once the matrix is populated it should call its _draw_cell() method on each Cell
    '''
    for i in range(self._num_cols):
      # note the outer loop should increment shift the start point of the cell x1 by (x1+cell_size*i)
      col_list = []
      for j in range(self._num_rows):
        # note each pass of the inner loop should should shift the start of the y point
        col_list.append(Cell(self._win))
      self._cells.append(col_list)
      
    for i in range(self._num_cols):
      for j in range(self._num_rows):
        self._draw_cell(i,j)

  def _draw_cell(self, i, j):
    ''' 
    This method should calculate the x/y position of the Cell based on i, j, the cell_size, and the x/y position of the Maze itself

    The x/y position of the maze represents how many pixels from the top and left the maze should start from the side of the window

    Once calculated, it should draw the cell and call the maze's _animate() method
    '''
    
    if self._win is None:
      return

    x1 = self._x1 + i * self._cell_size_x
    x2 = x1 + self._cell_size_x
    y1 = self._y1 + j* self._cell_size_y
    y2 = y1 + self._cell_size_y

    self._cells[i][j].draw_cell(x1, y1, x2, y2)
    self._animate()
  
  def _animate(self):
    ''' 
    Allows us to visualize what the algorithms are doing in real time.

    It should call the window's redraw() method, then use time.sleep() for a short amount of time so your eyes keep up with each render frame (0.05 seconds)
    '''
    if self._win is None:
      return 

    self._win.redraw()
    time.sleep(0.10)
  
  def _break_entrance_and_exit(self):
    ''' 
    Should remove the top wall from the first cell in the self._cells list of list (ie. self._cells[0][0]) and the bottom wall from the last cell (ie. self._cells[num_cols-1][num_rows-1])
    '''
    self._cells[0][0].has_top_wall = False
    self._draw_cell(0,0)
    self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
    self._draw_cell(self._num_cols-1, self._num_rows-1)
    

  def _break_walls_r(self, i, j):
    pass
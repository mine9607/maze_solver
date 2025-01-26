
from cells import Cell

import time
class Maze:
  def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
    self._cells = []
    self._x1 = x1
    self._y1 = y1
    self._num_rows = num_rows
    self._num_cols = num_cols
    self._cell_size_x = cell_size_x
    self._cell_size_y = cell_size_y
    self._win = win

    self._create_cells()
  
  def _create_cells(self):
    pass
    '''  
    This function should fill a self.__cells list with lists of cells

    Each top-level list is a column of Cell Objects.

    Once the matrix is populated it should call its _draw_cell() method on each Cell
    '''
    for i in range(self.num_cols):
      # note the outer loop should increment shift the start point of the cell x1 by (x1+cell_size*i)
      col_list = []
      for j in range(self.num_rows):
        # note each pass of the inner loop should should shift the start of the y point
        x1 = self._x1 + self._cell_size_x*i
        x2 = x1 + self._cell_size_x

        y1 = self._y1 + self._cell_size_y*j
        y2 = y1 + self._cell_size_y

        # Create a cell object 
        cell = Cell(x1 = x1, x2 = x2, y1 = y1, y2 = y2,win = self.__win, left_wall=True, right_wall=True, top_wall= True, bottom_wall=True)
        col_list.append(cell)
        # self.__draw_cell(i,j)  
        # NOTE: why call self.__draw_cell when the Cell class already has a draw_cell(self) method? - Note because we need to call self.__animate()
        cell.draw_cell()
        self.__animate()

      self.__cells.append(col_list)

  def __draw_cell(self, i, j):
    pass

    ''' 
    This method should calculate the x/y position of the Cell based on i, j, the cell_size, and the x/y position of the Maze itself

    The x/y position of the maze represents how many pixels from the top and left the maze should start from the side of the window

    Once calculated, it should draw the cell and call the maze's _animate() method
    '''
    # Calculate the cell 

    self._animate()
  
  def _animate(self):
    ''' 
    Allows us to visualize what the algorithms are doing in real time.

    It should call the window's redraw() method, then use time.sleep() for a short amount of time so your eyes keep up with each render frame (0.05 seconds)
    '''

    self._win.redraw()
    time.sleep(0.05)
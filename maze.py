
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
  
  def _create_cells(self):
    pass
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
        x1 = self._x1 + self._cell_size_x*i
        x2 = x1 + self._cell_size_x

        y1 = self._y1 + self._cell_size_y*j
        y2 = y1 + self._cell_size_y

        # Create a maze entrance
        if i == 0 and j == 0:
          cell = Cell(x1 = x1, x2 = x2, y1 = y1, y2 = y2,win = self._win, left_wall=True, right_wall=True, top_wall= False, bottom_wall=True)
          col_list.append(cell)
          cell.draw_cell()
          self._animate()

        
        # Create a maze exit
        elif i == self._num_cols-1 and j == self._num_rows-1:
          cell = Cell(x1 = x1, x2 = x2, y1 = y1, y2 = y2,win = self._win, left_wall=True, right_wall=True, top_wall= True, bottom_wall=False)
          col_list.append(cell)
          cell.draw_cell()
          self._animate()

        
        else:
          # Create a cell object 
          cell = Cell(x1 = x1, x2 = x2, y1 = y1, y2 = y2,win = self._win, left_wall=True, right_wall=True, top_wall= True, bottom_wall=True)
          col_list.append(cell)
          # self.__draw_cell(i,j)  
          # NOTE: why call self.__draw_cell when the Cell class already has a draw_cell(self) method? - Note because we need to call self.__animate()
          cell.draw_cell()
          self._animate()

      self._cells.append(col_list)

  def __draw_cell(self, i, j):
    pass

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

    self._cells[i][j].draw(x1, y1, x2, y2)
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
  
  def _break_entrance_and_exit():
    pass
    ''' 
    Should remove the top wall from the first cell in the self._cells list of list (ie. self._cells[0][0]) and the bottom wall from the last cell (ie. self._cells[num_cols-1][num_rows-1])
    '''
    self._cells[0][0].has_top_wall = False
    self._draw_cell(0,0)
    self._cells[num_cols-1][num_rows-1].has_bottom_wall = False
    self._draw_cell(self.num_cols-1, self.num_rows-1)
    

  def _break_walls_r(self, i, j):
    pass
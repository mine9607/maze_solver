
from cell import Cell
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
    self._break_walls_r(0,0)
    self._reset_cells_visited()
  
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
    self._animate_maze()
    # self.solve()
  
  def _animate_maze(self):
    ''' 
    Allows us to visualize what the algorithms are doing in real time.

    It should call the window's redraw() method, then use time.sleep() for a short amount of time so your eyes keep up with each render frame (0.05 seconds)
    '''
    if self._win is None:
      return 

    self._win.redraw()
    time.sleep(0.005)

  def _animate_solution(self):
    if self._win is None:
      return 

    self._win.redraw()
    time.sleep(0.1)
  
  def _break_entrance_and_exit(self):
    ''' 
    Should remove the top wall from the first cell in the self._cells list of list (ie. self._cells[0][0]) and the bottom wall from the last cell (ie. self._cells[num_cols-1][num_rows-1])
    '''
    self._cells[0][0].has_top_wall = False
    self._draw_cell(0,0)
    self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
    self._draw_cell(self._num_cols-1, self._num_rows-1)
    

  def _break_walls_r(self, i, j):
    self._cells[i][j].visited = True
    while True:
      need_to_visit = [] # list to hold the i and j values that need to be visited

      # Set bounds i-1 must be >=0; i+1 must be <= num-cols; j-1 mu
      

      # Check the cells adjacent to current cell
      # Check if the cell exists and if it's visited property is False
      if i-1 >= 0: 
        left_cell = self._cells[i-1][j]
        if not left_cell.visited:
          need_to_visit.append((i-1,j))
      if i+1 < self._num_cols:
        right_cell = self._cells[i+1][j]
        if not right_cell.visited:
          need_to_visit.append((i+1,j))
      if j-1 >= 0:
        top_cell = self._cells[i][j-1]
        if not top_cell.visited:
          need_to_visit.append((i, j-1))
      if j+1 < self._num_rows:
        bottom_cell = self._cells[i][j+1]
        if not bottom_cell.visited:
          need_to_visit.append((i, j+1))

      # If all adjacent cells have been "visited" then draw cell and exit via 'return'
      if len(need_to_visit) == 0:
        self._draw_cell(i,j)
        return
      
      # Pick a random direction of an adjacent cell
      next_i, next_j = random.choice(need_to_visit)

      # break the wall between the current cell and the next cell
      if next_i - i == 0 and next_j - j==1:
        self._cells[i][j].has_bottom_wall = False
        self._cells[next_i][next_j].has_top_wall = False
      if next_i - i == 0 and next_j - j == -1:
        self._cells[i][j].has_top_wall = False
        self._cells[next_i][next_j].has_bottom_wall = False
      if next_i - i == 1 and next_j - j ==0:
        self._cells[i][j].has_right_wall = False
        self._cells[next_i][next_j].has_left_wall = False
      if next_i - i == -1 and next_j -j ==0:
        self._cells[i][j].has_left_wall = False
        self._cells[next_i][next_j].has_right_wall = False


      # Draw the cells
      self._draw_cell(i,j)
      self._draw_cell(next_i, next_j)
      
      self._break_walls_r(next_i, next_j)

  def _reset_cells_visited(self):
    for i in range(self._num_cols):
      for j in range(self._num_rows):
        self._cells[i][j].visited = False

  def solve(self):
    return self._solve_r()
    # return True if the maze was solved
    # return False if the maze wasn't solved

  def _solve_r(self, i=0, j=0):
    # return True if the current cell is an 'end cell'
    # return True if the current cell leads to the 'end cell'
    # return False if the current cell is a loser cell

    self._animate_solution()
    current_cell = self._cells[i][j]
    current_cell.visited = True

    if i == self._num_cols-1 and j == self._num_rows-1:
      # solver has reached the end cell
      return True

    # For EACH DIRECTION:
      # Check if a cell exists in that direction && that no wall exists && the cell hasn't been visited

    # If there is a cell in that direction and no wall between cells,
        # Draw a move between the current cell and the next cell
        # Call _solve_r recursively with the next_i, next_j to move to that cell
            # if the cell returns True then return True
            # Else draw an "undo" move between the current cell and the next cell

    # while True:
    # Left Cell
    if i-1 >= 0:
      left_cell = self._cells[i-1][j]
      if not left_cell.visited and not current_cell.has_left_wall:
        current_cell.draw_move(left_cell)
        if self._solve_r(i-1,j):
          return True
        current_cell.draw_move(left_cell, undo=True)
          
    # Right Cell
    if i+1 < self._num_cols:
      right_cell = self._cells[i+1][j]
      if not right_cell.visited and not current_cell.has_right_wall:
        current_cell.draw_move(right_cell)
        if self._solve_r(i+1,j):
          return True
        current_cell.draw_move(right_cell, undo=True)

    # Top Cell
    if j-1 >= 0:
      top_cell = self._cells[i][j-1]
      if not top_cell.visited and not current_cell.has_top_wall:
        current_cell.draw_move(top_cell)
        if self._solve_r(i, j-1):
          return True
        current_cell.draw_move(top_cell, undo=True)
      
    # Bottom Cell
    if j+1 < self._num_rows:
      bottom_cell = self._cells[i][j+1]
      if not bottom_cell.visited and not current_cell.has_bottom_wall:
        current_cell.draw_move(bottom_cell)
        if self._solve_r(i, j+1):
          return True
        current_cell.draw_move(bottom_cell, undo=True)
    
    return False
      
  def _reset_cells_visited(self):
    for i in range(self._num_cols):
      for j in range(self._num_rows):
        self._cells[i][j].visited = False

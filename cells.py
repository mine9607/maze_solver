from draw import Point, Line

# NOTE: to improve code - refactor the draw_cell function to include a helper function draw_wall
# NOTE: refactor with a get_center method to get self.get_center() and to_cell.get_center()
# NOTE: Improve cell calculations with abs values in center calc
# NOTE: what if a negative value is passed to a point (i.e. x2 = -100)

class Cell:
  def __init__(self, x1, x2, y1, y2, win, left_wall=True, right_wall=True, top_wall=True, bottom_wall=True ):
    self.has_left_wall = left_wall
    self.has_right_wall = right_wall
    self.has_top_wall = top_wall
    self.has_bottom_wall = bottom_wall
    self._x1 = x1 # left point of the cell - horizontal
    self._x2 = x2 # right point of the cell - horizontal
    self._y1 = y1 # top point of the cell - vertical
    self._y2 = y2 # bottom point of the cell - vertical
    self._win = win

  def draw_cell(self, fill_color="black"):
    if self._win is None:
      return
    # If cell has walls draw them
    if self.has_top_wall:
      # draw line from start point (x1,y1) to (x2,y1)
      top_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
      self._win.draw_line(top_line, fill_color)
    else:
      self._win.draw_line(top_line, "white")
    
    if self.has_right_wall:
      # draw line from start point (x2,y1) to (x2,y2)
      right_line = Line(Point(self._x2, self._y1),Point(self._x2, self._y2))
      self._win.draw_line(right_line, fill_color)
    else:
      self._win.draw_line(right_line, "white")
    
    if self.has_bottom_wall:
      # draw line from start point (x2, y2) to (x1, y2)
      bottom_line = Line(Point(self._x2, self._y2),Point(self._x1, self._y2))
      self._win.draw_line(bottom_line, fill_color)
    else:
      self._win.draw_line(bottom_line, "white")

    if self.has_left_wall:
      # draw line from start point (x1,y2) to (x1,y1)
      left_line = Line(Point(self._x1, self._y2), Point(self._x1, self._y1))
      self._win.draw_line(left_line, fill_color)
    else:
      self._win.draw_line(left_line, "white")

  def draw_move(self, to_cell, undo=False):
    '''
    this method should draw a line between the CENTER of two cells

    if undo = false draw a red line
    else draw a gray line

    this allows us to visually see when our line is backtracking across a path previously drawn

    self and to_cell will both be instances of the Cell class and therefore have x/y coordinates
    '''
    if self._win is None:
      return

    self_center = Point(self.__x1 + (self.__x2 - self.__x1)/2, self.__y1+(self.__y2-self.__y1)/2)
    to_cell_center = Point(to_cell.__x1 + (to_cell.__x2 - to_cell.__x1)/2, to_cell.__y1 + (to_cell.__y2-to_cell.__y1)/2)
    
    connecting_line = Line(self_center, to_cell_center)

    fill_color = "gray" if undo else "red"
    self._win.draw_line(connecting_line, fill_color=fill_color)
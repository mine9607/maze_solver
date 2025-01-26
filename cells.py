from draw import Point, Line

# NOTE: to improve code - refactor the draw_cell function to include a helper function draw_wall

class Cell:
  def __init__(self, x1, x2, y1, y2, win, left_wall=True, right_wall=True, top_wall=True, bottom_wall=True ):
    self.has_left_wall = left_wall
    self.has_right_wall = right_wall
    self.has_top_wall = top_wall
    self.has_bottom_wall = bottom_wall
    self.__x1 = x1 # left point of the cell - horizontal
    self.__x2 = x2 # right point of the cell - horizontal
    self.__y1 = y1 # top point of the cell - vertical
    self.__y2 = y2 # bottom point of the cell - vertical
    self.__win = win

  def draw_cell(self, fill_color="black"):
    # If cell has walls draw them
    if self.has_top_wall:
      # draw line from start point (x1,y1) to (x2,y1)
      start_point = Point(self.__x1, self.__y1)
      end_point = Point(self.__x2, self.__y1)
      top_wall_line = Line(start_point, end_point)
      self.__win.draw_line(top_wall_line, fill_color)
    
    if self.has_right_wall:
      # draw line from start point (x2,y1) to (x2,y2)
      start_point = Point(self.__x2, self.__y1)
      end_point = Point(self.__x2, self.__y2)
      right_wall_line = Line(start_point, end_point)
      self.__win.draw_line(right_wall_line, fill_color)
    
    if self.has_bottom_wall:
      # draw line from start point (x2, y2) to (x1, y2)
      start_point = Point(self.__x2, self.__y2)
      end_point = Point(self.__x1, self.__y2)
      bottom_wall_line = Line(start_point, end_point)
      self.__win.draw_line(bottom_wall_line, fill_color)

    if self.has_left_wall:
      # draw line from start point (x1,y2) to (x1,y1)
      start_point = Point(self.__x1, self.__y2)
      end_point = Point(self.__x1, self.__y1)
      left_wall_line = Line(start_point, end_point)
      self.__win.draw_line(left_wall_line, fill_color)


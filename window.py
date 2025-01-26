from tkinter import Tk, BOTH, Canvas

class Window:
  # create a constructor function to setup the Window class with a root widget and canvas
  def __init__(self, width, height):
    # create a root widget using Tk()
    self.__root = Tk()
    # set the title on the root widget using the "title" method
    self.__root.title("Maze Solver")

    # Create a Canvas widget belonging to root with width and height properties
    self.__canvas = Canvas(self.__root,bg="white", width=width, height=height)

    # pack the canvas (arranges widgets in blocks before placing them in the parent widget (i.e. "root"))
    '''
    fill: determines whether the widget fills any extra space allocated to it by the packer or keeps its own minimal dimensions
      **options: NONE, X, Y, BOTH (default) => horizontal, vertical, both

    expand: when set to True, the widget expands to fill any space not otherwise used in the parent widget
    '''
    self.__canvas.pack(fill=BOTH, expand=True)

    # Set the window to "not be running" on class initialization
    self.__running = False

    self.__root.protocol("WM_DELETE_WINDOW", self.close)
  
  def draw_line(self, line, fill_color):
    # note line will be an instance of the Line class 
    line.draw(self.__canvas, fill_color=fill_color)


  # create a class function to redraw the window when executed
  def redraw(self):
    self.__root.update_idletasks()
    self.__root.update()
  
  def wait_for_close(self):
    self.__running=True
    
    while self.__running:
      self.redraw()
    print("window closed")

  def close(self):
    self.__running=False
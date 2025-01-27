# Building a Maze Solver in Python

## Architecture:

### 1. Window Class

The Window Class is responsible for defining a window object with a canvas widget using Tkinter

- It takes `width` and `height` as arguments in the constructor
- It should:
  1. Initialize the window and contain methods to:
     1. Draw a Line: `draw_line(self, line, fill_color)`
     2. Redraw the Window: `redraw(self)`
     3. Wait for Close: `wait_for_close(self)`
     4. Close the window: `close(self)`

### 2. Point Class

The Point Class is responsible for picking a point in the instantiated Window object

- It takes an `x` and `y` argument in the constructor:
  1. `x` and `y` represent coordinate positions (in pixels) relative to upper left of Window object at (0,0)
- It should:
  1. Initialize a point object with x and y properties - for use in drawing lines

### 3. Line Class

The Line Class is responsible for drawing a colored line between two instantiated points of the Point Class

- It takes `point1` and `point2` as arguments in the constructor
- It should:
  1. Initialize a line object and contain methods to:
     1. Draw a Line: `draw(self, canvas, point1, point2)`
        - uses the Canvas method: `canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)`

### 4. Cell Class

### 5. Maze Class

The Maze Class is responsible for:

1. Defining the shape (`num_cols` x `num_rows`) of the maze
2. Drawing the cells
3. Createing the path from entrance to exit
4. Drawing the solver

- It takes `self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None` as arguments in the constructor
- It should:
  1. Initialize a maze object and contain methods to:
     1. Create the cells defining the maze: `create_cells(self)`
     2. Animate the drawing of the maze: `_animate(self)`
        - Should call the `Window.redraw()` method with a sleep time to visually see the rendering of the cells (use the time package => time.sleep(0.05))

from window import Window
from draw import Point, Line
from cells import Cell

win = Window(800, 600)

#Create points
point1 = Point(100, 100)
point2 = Point(300, 100)
point3 = Point(300, 300)
point4 = Point(100, 300)

# Create lines connecting the points
line1 = Line(point1, point2)
line2 = Line(point1, point3)
line3 = Line(point1, point4)
line4 = Line(point4, point2)

win.draw_line(line1, fill_color="red")
win.draw_line(line2, fill_color="blue")
win.draw_line(line3, fill_color="green")
win.draw_line(line4, fill_color="purple")

cell1 = Cell(500, 550, 100, 150, win, top_wall=False) # no top wall
cell1.draw_cell(fill_color="red")

cell2 = Cell(550, 600, 150, 200, win, right_wall=False) # no right wall
cell2.draw_cell()

cell3 = Cell(500, 550, 200, 250, win, bottom_wall=False) # no bottom wall
cell3.draw_cell(fill_color="green")

cell4 = Cell(450, 500, 150, 200, win, left_wall=False) # no left wall
cell4.draw_cell(fill_color="blue")

win.wait_for_close()
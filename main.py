from window import Window
from draw import Point, Line

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



win.wait_for_close()
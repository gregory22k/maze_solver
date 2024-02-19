from graphics import *


class Cell:
    # maze cell class
    # initially a cell has every wall and is not visited by any searching algorithm
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        # x1, y1, x2, y2 represent the 4 corners of the cell
        # and based on the boolean attributes, we draw the sides
        # or use black color as the background in order to
        # "destroy" the wall
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if not self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if not self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if not self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        if not self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "black")

    # method to create a path between 2 cells
    # if the undo value is True, the color is set to gray
    # and thus indicates a non-valid path to the exit
    # otherwise the green path indicates the correct path to the exit
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        line = Line(Point((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2), Point((to_cell.x1 + to_cell.x2) / 2,
                                                                                   (to_cell.y1 + to_cell.y2) / 2))
        fill_color = "gray" if undo else "green"
        self._win.draw_line(line, fill_color)

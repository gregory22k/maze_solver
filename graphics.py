from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        """

        :rtype: object
        """
        self.__root = Tk()
        self.__root.title("Maze Solver")

        self.__canvas = Canvas(self.__root, bg="black", width=width, height=height)
        self.__canvas.pack(expand=True, fill=BOTH)

        self.__running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="white"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False

# class that represents a point with (x, y) coordinates
# used for drawing lines between 2 points
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# class that helps with drawing a line between 2 points
class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color="white"):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y,
                           fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=True)

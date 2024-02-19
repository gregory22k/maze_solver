from cell import Cell
import random
import time


class Maze:
    # a maze is consisted of rows, columns -> matrix of cells
    # and the size of the cells
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self.solved = False
        if seed:
            random.seed(seed)

        self._create_cells()  # initialize cells matrix
        self._break_entrance_and_exit()  # create opening at the start and end of maze
        self._break_walls_r(0, 0)   # break walls and actually create the pattern of the maze
        self._reset_cells_visited()      # reset visited value for all cells, so that the _solve_r method can work

    # instantiates the cells and draws them to the window
    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    # based on the cell's size and the i, j indices
    # this method draws the cell
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    # animated creation of the maze
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.03)

    # create entrance and exit for the maze
    # by painting black the left and right wall of the first and last cell correspondingly
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        # set the cell as visited
        self._cells[i][j].visited = True

        while True:
            next_index_list = []  # determine which cell(s) to visit next by appending them to the list

            # left cell
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right cell
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # top cell
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # bottom cell
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))
            if not next_index_list:
                self._draw_cell(i, j)
                return
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # destroy the walls between the cell and the to_visit cell
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    # solver method that calls the recursive solver method
    # created to hide the complexity of the actual solver method
    def solve(self):
        return self._solve_r(0, 0)

    # recursive method to solve the maze
    def _solve_r(self, i, j):
        # call animate method and set the initial cell as visited
        self._animate()
        self._cells[i][j].visited = True

        # set the goal cell and create the base case
        goal = self._cells[self._num_cols- 1][self._num_rows - 1]
        if self._cells[i][j] == goal:
            return True

        # check for valid cells to visit
        # if the result is True for the next cell, it means we found the exit, and the maze is solved
        # else call this method recursively for the next cell
        if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        if i < self._num_cols - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        if j + 1 < self._num_rows and not self._cells[i][j + 1].visited and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False

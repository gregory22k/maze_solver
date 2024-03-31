# Maze Solver App

This Maze Solver application is built with Python and Tkinter. It generates random mazes and provides functionality to solve them using a recursive depth-first search algorithm. Below is a brief overview of the functionality and structure of the application:

<img width="400" alt="image" src="https://github.com/gregory22k/maze_solver/assets/88857864/63b86498-92de-48e7-8ecb-105b3708f696">


## Features

- **Random Maze Generation**: The application creates random mazes of varying sizes with entrance and exit points.
- **Maze Solving**: It employs a recursive depth-first search algorithm to find a path from the entrance to the exit of the maze.
- **Visualization**: The maze generation and solving process are visualized using Tkinter, providing an animated display of the algorithm in action.

## Maze Generation

The maze generation process starts with a grid of cells. Walls are randomly removed between adjacent cells to create a maze pattern. Entrance and exit points are established, allowing for traversal from the start to the end of the maze.

## Maze Solving Algorithm

The maze solving algorithm is a recursive depth-first search (DFS) method. It explores paths within the maze, attempting to find a route from the start cell to the goal cell. The process involves marking cells as visited, exploring neighboring cells, and backtracking when necessary until a solution path is found.

## Usage

To use the Maze Solver application, simply run the Python script. The application will generate a random maze and display it on the screen. You can watch as the algorithm navigates through the maze to find the solution.

## Dependencies

The application requires Python and Tkinter to be installed.

## Contributing

Contributions to this project are welcome. You can fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).


## How to Use

To use the maze solver app, simply run the Python script. The maze will be displayed, and you can watch as the algorithm navigates through it to find the solution. You can change the size of the maze simply by changing the `num_rows` and `num_cols` in the main function.

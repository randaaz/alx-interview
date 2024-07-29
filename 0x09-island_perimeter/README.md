# 0x09. Island Perimeter

## Project Overview

The goal of this project is to calculate the perimeter of an island represented in a grid (2D array). The grid is composed of integers where `0` represents water and `1` represents land. The perimeter is calculated by counting the number of edges of land cells that are adjacent to water or the grid boundary.

## Requirements

- **Editors**: vi, vim, emacs
- **Interpreter**: Python 3 (version 3.4.3)
- **Operating System**: Ubuntu 20.04 LTS
- **Coding Standards**: PEP 8 (version 1.7)
- **Other**:
  - Do not import any external modules.
  - All code must be documented.
  - All files must be executable.

## Concepts Needed

### 2D Arrays (Matrices)
- **Access and Iteration**: Navigating through each element in a 2D array.
- **Adjacent Cells**: Moving horizontally and vertically to adjacent cells.

### Conditional Logic
- **Cell Contribution**: Determine if a cell contributes to the island's perimeter based on surrounding water or boundary conditions.

### Counting Techniques
- **Edge Counting**: Methodology to count the edges of land cells that contribute to the perimeter.

### Problem-Solving Strategies
- **Breaking Down the Problem**: Identifying land cells and calculating their contribution to the perimeter.

## Resources

- **Python Official Documentation**:
  - [Nested Lists](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions)

- **GeeksforGeeks Articles**:
  - [Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/)

- **TutorialsPoint**:
  - [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)

- **YouTube Tutorials**:
  - [Python 2D arrays and lists](https://www.youtube.com/results?search_query=python+2d+arrays+and+lists)

## Task: Island Perimeter

### Objective
Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in the grid.

### Specifications
- **Grid**: A list of lists of integers:
  - `0` represents water.
  - `1` represents land.
  - Each cell is square with a side length of 1.
  - Cells are connected horizontally/vertically (not diagonally).
  - The grid is rectangular with a maximum width and height of 100.
  - The grid is completely surrounded by water.
  - There is only one island or no island at all.
  - The island does not contain lakes (water inside that isn’t connected to the surrounding water).

### Example
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(island_perimeter(grid))  # Output: 12


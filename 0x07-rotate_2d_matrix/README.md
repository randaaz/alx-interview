# 0x07. Rotate 2D Matrix

## Algorithm
Python

### Objective
Implement an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise.

### Key Concepts
1. **Matrix Representation in Python:**
   - Understanding 2D matrices using lists of lists in Python.
   - Accessing and modifying elements in a 2D matrix.

2. **In-place Operations:**
   - Performing operations on data without creating a copy.
   - Minimizing space complexity by modifying the matrix in place.

3. **Matrix Transposition:**
   - Concept of transposing a matrix (swapping rows and columns).
   - Implementing transposition as a step in the rotation process.

4. **Reversing Rows in a Matrix:**
   - Manipulating rows by reversing their order for rotation.

5. **Nested Loops:**
   - Using nested loops to iterate through 2D matrices.
   - Modifying elements within nested loops to achieve rotation.


### Additional Resources
- Mock Technical Interview

### Requirements
- **General:**
  - Allowed editors: `vi`, `vim`, `emacs`
  - Files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.10)
  - Files should end with a new line
  - First line of all files should be exactly `#!/usr/bin/python3`
  - A `README.md` file, at the root of the project folder, is mandatory
  - Code should use the pycodestyle style (version 2.8.0)
  - No module imports allowed
  - All modules and functions must be documented
  - All files must be executable

### Tasks
#### 0. Rotate 2D Matrix
**Mandatory**

Rotate an n x n 2D matrix 90 degrees clockwise.

- **Prototype:** `def rotate_2d_matrix(matrix):`
- **Note:** Do not return anything. The matrix must be edited in-place.
- **Assumptions:** The matrix will have 2 dimensions and will not be empty.

```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)


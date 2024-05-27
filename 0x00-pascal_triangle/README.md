# 0x00. Pascal's Triangle

## Description

This project involves creating an algorithm in Python to generate Pascal's Triangle, a triangular array of binomial coefficients. The goal is to practice essential Python concepts such as list comprehensions, functions, loops, and conditional statements, while also understanding and implementing the mathematical logic behind Pascal's Triangle.

## Learning Objectives

To successfully complete this project, you should be able to:

- Understand how to create, access, modify, and iterate over lists.
- Utilize list comprehensions for concise and readable code.
- Define and call functions, pass parameters, and return values.
- Use for and while loops to iterate through sequences and generate Pascal's Triangle.
- Apply if, elif, and else conditions to implement logic within the triangle.
- (Optional) Understand recursion and apply it to generate Pascal's Triangle.
- Perform arithmetic operations to calculate each element of Pascal's Triangle.
- Access elements and slices of lists for constructing each row of the triangle.
- Be mindful of memory management when creating new rows.
- (Optional) Handle potential errors using try-except blocks.
- Consider the time and space complexity of different approaches and optimize your solution.

## Tasks

### 0. Pascal's Triangle

**Mandatory**

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:

- Returns an empty list if `n <= 0`
- You can assume `n` will always be an integer

#### Example

```python
guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$


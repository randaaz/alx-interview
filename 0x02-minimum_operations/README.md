# 0x02. Minimum Operations

## Project Overview
This project focuses on calculating the minimum number of operations required to achieve a given number of characters in a text file using only "Copy All" and "Paste" operations. You will employ various algorithmic and mathematical concepts to devise an efficient solution.

## Concepts
To complete this project, you should familiarize yourself with the following concepts and resources:

### Dynamic Programming
- Helps in breaking down the problem into simpler subproblems and building up the solution.

### Prime Factorization
- Understanding prime factorization is crucial since the problem can be reduced to finding the sum of the prime factors of the target number n.

### Code Optimization
- Approaching problems from an optimization perspective can help find the most efficient solution.

### Greedy Algorithms
- The problem can be approached with greedy algorithms, choosing the best option at each step.

### Basic Python Programming
- Proficiency in Python, including loops, conditionals, and functions, is necessary to implement the solution.

By studying these concepts and utilizing the resources provided, you will be equipped to tackle the “Minimum Operations” problem effectively, applying both mathematical reasoning and programming skills to find the most efficient solution.

## Additional Resources
- Mock Technical Interview

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`.
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3).
- All files should end with a new line.
- The first line of all files should be `#!/usr/bin/python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code should be documented.
- Code should follow the PEP 8 style (version 1.7.x).
- All files must be executable.

## Task

### Task 0: Minimum Operations
In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

**Prototype**: `def minOperations(n)`
- Returns an integer.
- If `n` is impossible to achieve, return 0.

Example:
```python
n = 9

H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6


# 0x08. Making Change

## Project Overview

The "0x08. Making Change" project involves solving the classic coin change problem using dynamic programming and greedy algorithms. The goal is to determine the minimum number of coins required to make up a given total amount from a list of coin denominations.

### Key Concepts

- **Greedy Algorithms:** Understand how greedy algorithms work, their suitability for the coin change problem, and their limitations.
- **Dynamic Programming:** Learn basic principles, overlapping subproblems, and optimal substructure in the context of coin change.
- **Algorithmic Complexity:** Analyze time and space complexity to create efficient solutions.
- **Problem-Solving Strategies:** Break down problems into smaller sub-problems and choose between iterative and recursive approaches.
- **Python Programming:** Use lists, list comprehensions, and implement functions with efficient looping and conditional statements.



### Requirements

- **Editors:** Allowed editors include vi, vim, and emacs.
- **Environment:** All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3).
- **File Format:** All files should end with a new line. The first line of all files should be `#!/usr/bin/python3`.
- **PEP 8 Style:** Your code should adhere to the PEP 8 style guide (version 1.7.x).
- **Executability:** All files must be executable.

### Tasks

#### 0. Change comes from within

**Prototype:**
```python
def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

    Args:
    coins (List[int]): List of coin values.
    total (int): Total amount to make change for.

    Returns:
    int: Fewest number of coins needed to meet total. Returns 0 if total is 0 or less. Returns -1 if total cannot be met by any number of coins.
    """


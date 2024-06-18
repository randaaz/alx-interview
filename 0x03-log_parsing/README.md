# 0x03. Log Parsing

## Overview

The "0x03. Log Parsing" project involves creating a Python script to parse and process log data in real-time from standard input (stdin). The script reads log entries, processes the data to compute various metrics, and outputs the results. This project focuses on several key Python programming concepts, including file I/O, signal handling, data processing, regular expressions, dictionaries, and exception handling.

## Requirements

- **Editors**: vi, vim, emacs
- **Operating System**: Ubuntu 20.04 LTS
- **Python Version**: 3.4.3
- **Code Style**: PEP 8 (version 1.7.x)
- **File Endings**: All files should end with a new line
- **Shebang**: The first line of all files should be exactly `#!/usr/bin/python3`
- **Execution**: All files must be executable
- **Length Check**: File lengths will be tested using `wc`
- **README**: A `README.md` file at the root of the project directory is mandatory

## Concepts Needed

### File I/O in Python
- Reading from `sys.stdin` line by line.


### Signal Handling in Python
- Handling keyboard interruption (CTRL + C) using signal handling.
-### Data Processing
- Parsing strings to extract specific data points.
- Aggregating data to compute summaries.

### Regular Expressions
- Using regular expressions to validate the format of each line.


### Dictionaries in Python
- Using dictionaries to count occurrences of status codes and accumulate file sizes.


### Exception Handling
- Handling possible exceptions that may arise during file reading and data processing.

## Project Tasks

### Task 0: Log Parsing (Mandatory)

**Objective**: Write a script that reads from stdin line by line and computes metrics.


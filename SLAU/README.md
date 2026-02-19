# SLAU Solver

A Python implementation of the Gaussian elimination method with column-wise partial pivoting for solving systems of linear algebraic equations (SLAU).

## Features
- Reads a square matrix and right-hand side vector from a text file
- Performs forward elimination with pivoting
- Back substitution to find the solution vector

## Usage
1. Prepare a `matrix.txt` file (first line: matrix size, then rows with coefficients separated by '|' from the right-hand side)
2. Run `python main.py`
3. The solution vector will be printed in the console
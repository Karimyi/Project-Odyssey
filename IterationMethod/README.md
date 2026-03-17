# Iteration Method Calculator

A console-based application for finding roots of equations using the simple iteration method (fixed-point iteration). The program calculates derivatives symbolically and performs iterative approximations to find the root of a given mathematical expression within a specified interval.

## Features
- Symbolic differentiation using SymPy
- Automatic calculation of the iteration parameter λ based on maximum derivative
- Support for various mathematical functions (exp, log, sin, cos, etc.)
- Configurable number of iterations
- Convergence detection with tolerance checking
- English interface with clear output formatting
- Error handling for invalid inputs and mathematical expressions

## Supported Mathematical Operations
- Basic arithmetic: `+`, `-`, `*`, `/`
- Powers: `^` or `**` (e.g., `x^2` or `x**2`)
- Constants: `e`, `pi`
- Functions: `exp()`, `log()`, `sin()`, `cos()`, `sqrt()`

### Example Expressions
- `x^2 - 2` (square root of 2)
- `x^3 + exp(-2*x)` (exponential equation)
- `cos(x) - x` (transcendental equation)
- `x^3 - x^2 + 2*x - 8` (cubic equation)

## Getting Started

### Prerequisites
- Python 3.x
- Required packages: `sympy` (mathematical symbolics)

Install the required package:
```bash
pip install sympy
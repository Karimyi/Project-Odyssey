import sympy as sp
import math

def calculate(expression, x):
    expr_with_value = expression.replace('^', '**')
    expr_with_value = expr_with_value.replace('x', str(x))
    context = {
        'e': math.e,
        'pi': math.pi,
        'sin': math.sin,
        'cos': math.cos,
        'exp': math.exp,
        'log': math.log,
        'sqrt': math.sqrt
    }
    return eval(expr_with_value, {"__builtins__": {}}, context)

def iteration_method(a, b, expression, count):
    a, b, count = float(a), float(b), int(count)
    x = sp.Symbol('x')
    expr_str = expression.replace('^', '**')
    f = sp.sympify(expr_str)
    f_prime = sp.diff(f, x)
    x_current = (a + b) / 2
    f_prime_first = abs(calculate(str(f_prime), a))
    f_prime_second = abs(calculate(str(f_prime), b))
    max_derivative = max(f_prime_first, f_prime_second)
    if max_derivative != 0:
        lam = 1 / max_derivative
    else:
        lam = 0.1
        print("Warning: derivative is 0, using λ = 0.1")
    iteration = 0
    while iteration < count:
        f_x = calculate(expression, x_current)
        x_next = x_current - lam * f_x
        if abs(x_next - x_current) < 1e-10:
            print(f"\nConvergence achieved! Root: {x_next:.8f}")
            return x_next
        x_current = x_next
        iteration += 1
    print(f"\nResult after {count} iterations: x = {x_current:.8f}")
    return x_current

def main():
    while True:
        try:
            a = input('Start of the root range: ')
            b = input('End of the root range: ')
            expression = input('Mathematical expression: ')
            count = input('Number of iterations: ')
            iteration_method(a, b, expression, count)
            cont = input('\nContinue? (y/n): ')
            if cont.lower() != 'y':
                break
        except Exception as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    main()
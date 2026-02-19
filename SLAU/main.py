import numpy as np

def gauss_forward(A, b):
    n = len(A)
    A = [row[:] for row in A]
    b = b[:]
    for k in range(n-1):
        # Finding the pivot element
        max_row = max(range(k, n), key=lambda i: abs(A[i][k]))
        if max_row != k:
            A[k], A[max_row] = A[max_row], A[k]
            b[k], b[max_row] = b[max_row], b[k]
    return A, b

def elimination(A, b):
    n = len(A)
    for k in range(n-1):
        for i in range(k+1, n):
            factor = A[i][k] / A[k][k]
            # Updating the row and right-hand side
            for j in range(k, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]
            A[i][k] = 0.0
    return A, b

def back_substitution(A, b):
    n = len(A)
    x = [0] * n
    for i in range(n-1, -1, -1):
        # Computing xi
        x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i+1, n))) / A[i][i]
    return x

def read_system(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        A = []
        b = []
        for line in f:
            left, right = line.strip().split('|')
            A.append([float(x) for x in left.split()])
            b.append(float(right))
    return A, b

def main():
    A, b = read_system("matrix.txt")
    # Solving the system
    A_perm, b_perm = gauss_forward(A, b)
    A_tri, b_tri = elimination(A_perm, b_perm)
    solution = back_substitution(A_tri, b_tri)
    print(solution)

if __name__ == "__main__":
    main()
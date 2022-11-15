from z3 import *

n = input("Please input a number: ")
n = int(n)

# We know each queen must be in a different row.
# So, we represent each queen by a single integer: the column position
Q = [ Int(f"Q_{row + 1}") for row in range(n) ]

# Each queen is in a column {1, ... n }
val_c = [ And(1 <= Q[row], Q[row] <= n) for row in range(n) ]

# At most one queen per column
col_c = [ Distinct(Q) ]

# Diagonal constraint
diag_c = [ If(i == j,
              True,
              And(Q[i] - Q[j] != i - j, Q[i] - Q[j] != j - i))
           for i in range(n) for j in range(i) ]

solve(val_c + col_c + diag_c)
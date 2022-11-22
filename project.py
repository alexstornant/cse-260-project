from z3 import *

n = int(input("Please input a number: "))

# Queen is in position Q[i][j], if Q[i][j] == 1, else 0
Q = [ [Int(f"Q_{i + 1}_{j + 1}") for j in range(n) ] for i in range(n) ]

Q_1 = [ And(Or( [Q[i][j] == 1 for j in range(n)] ) ) for i in range(n)]

Q_2 = [ And( [ And( [ And( Or( Not(Q[i][j] == 1), Not(Q[i][k] == 1) ) ) for k in range(j+1, n) ] ) for j in range(n-1) ]) for i in range(n) ]

Q_3 = [ And( [ And( [ And( Or( Not(Q[i][j] == 1), Not(Q[k][j] == 1) ) ) for k in range(i+1, n) ] ) for i in range(n-1) ]) for j in range(n) ]

Q_4 = [ And( [ And( [ And( Or( Not(Q[i][j] == 1), Not(Q[i-k][k+j] == 1) ) ) for k in range(min( i - 1, n - j)) ] ) for j in range(n-1) ]) for i in range(n) ]

Q_5 = [ And( [ And( [ And( Or( Not(Q[i][j] == 1), Not(Q[i+k][k+j] == 1) ) ) for k in range(min( n - i, n - j)) ] ) for j in range(n-1) ]) for i in range(1, n-1) ]

solve(Q_4 + Q_5)
print()
solve(Q_1 + Q_2 + Q_3)
print()
solve(Q_1 + Q_2 + Q_3 + Q_4 + Q_5)


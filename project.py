from z3 import *
import numpy as np
import matplotlib.pyplot as plt

n = int(input("Please input a number: "))

# Queen is in position Q[i][j], if Q[i][j] == 1, else Q[i][j] != 0
Q = [ [Int(f"Q_{i + 1}_{j + 1}") for j in range(n) ] for i in range(n) ]

Q_1 = And([ (Or( [Q[i][j] == 1 for j in range(n)] ) ) for i in range(n)])

Q_2 = And([Or( Not(Q[i][j] == 1), Not(Q[i][k] == 1) ) for i in range(n) for j in range(n-1) for k in range(j+1,n)])

Q_3 = And([Or( Not(Q[i][j] == 1), Not(Q[k][j] == 1) ) for j in range(n) for i in range(n-1) for k in range(i+1,n)])

Q_4 = And([Or(Not(Q[i][j] == 1), Not(Q[i-k][k+j] == 1)) for i in range(1, n) for j in range(n-1) for k in range(min(i-1, n-j))])

Q_5 = And([Or(Not(Q[i][j] == 1), Not(Q[i+k][k+j] == 1)) for i in range(n-1) for j in range(n-1) for k in range(min(n-i, n-j))])

s = Solver()
s.add(Q_1, Q_2, Q_3)
s.add(Q_4)
s.add(Q_5)

try:
   s.check()

   m = s.model()
   board = np.zeros((n,n))

   for i in range(n):
      for j in range(n):
         if m[Q[i][j]] == 1:
            board[i][j] = 10

   plt.matshow(board)
   plt.show()

except:
   print(s.check())
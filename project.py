from z3 import *

# Optional imports
import numpy as np
import matplotlib.pyplot as plt
# End optional

n = int(input("Please input a number: "))

# Queen is in position Q[i][j], if Q[i][j] == 1, else Q[i][j] != 0
Q = [ [Int(f"Q_{i + 1}_{j + 1}") for j in range(n) ] for i in range(n) ]

Q_1 = And([ Or( [Q[i][j] == 1 for j in range(n)] )  for i in range(n)])

Q_2 = And( [ And ( [ And( [Or( Not(Q[i][j] == 1), Not(Q[i][k] == 1)) for k in range(j+1,n)] )  for j in range(n-1)]) for i in range(n)] )

Q_3 = And( [ And ( [ And( [Or( Not(Q[i][j] == 1), Not(Q[k][j] == 1)) for k in range(i+1,n)] )  for i in range(n-1)]) for j in range(n)] )

Q_4 = And( [ And ( [ And( [Or( Not(Q[i-1][j-1] == 1), Not(Q[i-k-1][k+j-1] == 1)) for k in range(1, min(i-1,n-j) + 1)] )  for j in range(1,n)]) for i in range(2,n+1)] )
pp(Q_4)

Q_5 = And( [ And ( [ And( [Or( Not(Q[i-1][j-1] == 1), Not(Q[i+k-1][k+j-1] == 1)) for k in range(1,min(n-i,n-j)+1)] )  for j in range(1,n)]) for i in range(1,n)] )

s = Solver()
s.add(Q_1, Q_2, Q_3, Q_4, Q_5)

try:
   s.check()

   m = s.model()
   print(s.check())
   print(m)

   # Optional code to show board
   board = np.zeros((n,n))

   for i in range(n):
      for j in range(n):
         if m[Q[i][j]] == 1:
            board[i][j] = 10

   plt.matshow(board)
   plt.grid()
   plt.xticks(np.arange(0.5,n,step=1))
   plt.yticks(np.arange(0.5,n,step=1))
   plt.set_cmap("Greens")
   plt.show()
   # End optional

except:
   print(s.check())
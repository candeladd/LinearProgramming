#Andrew Candelaresi
# 
#HW4 Linear Programming
#P3

import sys
from pulp import*

x1 = LpVariable("1", 0 )
x2 = LpVariable("2", 0 )
x3 = LpVariable("3", 0 )
x4 = LpVariable("4", 0 )
x5 = LpVariable("5", 0 )
x6 = LpVariable("6", 0 )


prob = LpProblem("PractiveProblem", LpMaximize)

prob += (-2*x1)+(-3*x2)+(-1*x3)+(-1*x4)+(0*x5)+(1*x6)

prob += (1*x1)+(-1*x2)+(0*x3)+(0*x4)+(0*x5)+(-1*x6)<=3
prob += (1*x1)+(0*x2)+(0*x3)+(-1*x4)+(-1*x5)+(0*x6)<=-1
prob += (0*x1)+(0*x2)+(-1*x3)+(0*x4)+(0*x5)+(1*x6)<=-2
prob += (0*x1)+(-1*x2)+(-1*x3)+(1*x4)+(0*x5)+(1*x6)<=4
prob += (1*x1)+(0*x2)+(1*x3)+(0*x4)+(1*x5)+(1*x6)<=6
prob += (-1*x1)+(0*x2)+(0*x3)+(-1*x4)+(1*x5)+(-1*x6)<=-2


prob.writeLP("PracticeProblem.lp")
status =  prob.solve()

print("status = ", LpStatus[status])
print(x1.name, "=", x1.varValue)
print(x2.name, "=", x2.varValue)
print(x3.name, "=", x3.varValue)
print(x4.name, "=", x4.varValue)
print(x5.name, "=", x5.varValue)
print(x6.name, "=", x6.varValue)

print("optimal solution = ", value(prob.objective))

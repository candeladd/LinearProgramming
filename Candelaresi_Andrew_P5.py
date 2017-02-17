#Andrew Candelaresi
# 
#HW1 Linear Programming
#Diet Problem
#P5

import sys
from pulp import *

# variables
x1 = LpVariable("cookie", 0 )
x2 = LpVariable("Ramen", 0 )
x3 = LpVariable("Rice", 0)
x4 = LpVariable("Broccoli", 0)
x5 = LpVariable("CornFlakes", 0)


prob = LpProblem("myProblem", LpMinimize)
# add objective
prob += (.5*x1)+(2.5*x2)+(.25*x3)+(.2*x4)+(.6*x5)

#add constraints
prob += (300*x1) + (550*x2) + (450*x3)+(25*x4)+(300*x5) <=2200
prob += (20*x1) + (25*x2) + (25*x3)+(4*x4)+(15*x5) <=100
prob += (5*x1) + (8*x2) + (4*x3)+(2*x4)+(3*x5) <=80
prob += (10*x1) + (20*x2) + (.5*x3)+(.5*x4)+(.5*x5) <=100
prob += (.1*x1) + (.9*x2) + (.1*x3)+(.1*x4)+(.1*x5) <=5

prob += (300*x1) + (550*x2) + (450*x3)+(25*x4)+(300*x5) >=1800
prob += (20*x1) + (25*x2) + (25*x3)+(4*x4)+(15*x5) >=50
prob += (5*x1) + (8*x2) + (4*x3)+(2*x4)+(3*x5) >=30
prob += (10*x1) + (20*x2) + (.5*x3)+(.5*x4)+(.5*x5) >=60
prob += (.1*x1) + (.9*x2) + (.1*x3)+(.1*x4)+(.1*x5) >=3

prob.writeLP("DietProblemEC.lp")


prob += .5*((300*x1) + (550*x2) + (450*x3)+(25*x4)+(300*x5)) >= (300*x1)
prob += .5*((300*x1) + (550*x2) + (450*x3)+(25*x4)+(300*x5)) >= (550*x2)
prob += .5*((300*x1) + (550*x2) + (450*x3)+(25*x4)+(300*x5)) >= (450*x3)
prob += .5*((300*x1) + (550*x2) + (450*x3)+(25*x4)+(300*x5)) >= (25*x4)
prob += .5*((300*x1) + (550*x2) + (450*x3)+(25*x4)+(300*x5)) >= (300*x5)


# solve
status =  prob.solve()

print("status = ", LpStatus[status])
print(x1.name, "=", x1.varValue)
print(x2.name, "=", x2.varValue)
print(x3.name, "=", x3.varValue)
print(x4.name, "=", x4.varValue)
print(x5.name, "=", x5.varValue)
print("Total Cost of Food = ", value(prob.objective))

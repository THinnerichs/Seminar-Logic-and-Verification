import cdd
import numpy as np

b = np.array([2000,55,800,-100,-5,-10,-2,0,0,0]).reshape(-1,1)
b = b* -1
A = np.array([[350,80,340],[15,4,7],[40,130,30],[-10,-4,-20],[-1,0,0],[0,-1,0],[0,0,-1],[1,0,0],[0,1,0],[0,0,1]])

bA = np.hstack((b,A))

print('bA', bA)


mat = cdd.Matrix(bA)
mat.rep_type = cdd.RepType.INEQUALITY

poly = cdd.Polyhedron(mat)
print('poly', poly) 
print('poly.get_gen', poly.get_generators()) 


# Sage stuff
from sage.all import *
import subprocess

L = []
nt = cdd.NumberTypeable('float')
for _,x,y,z in poly.get_generators():
    L.append((nt.make_number(x),nt.make_number(y),nt.make_number(z)))

print(L)

filename = '3d_polytope_command'
with open(file=filename, mode='w') as f:
    ex = "sage -c "
    start = "'P1 = Polyhedron(vertices="+str(L)+");"
    end = "P1.plot()'"
    f.write(ex+start+end)

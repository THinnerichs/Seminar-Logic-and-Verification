import cdd

mat = cdd.Matrix([[1,-1,0,1],[1,0,-1,1],[1,1,0,1],[1,0,1,1],[0,0,0,-1]])
# mat = cdd.Matrix([[1,1,0,-1],[1, 0,1,-1],[1,-1,0,-1],[1,0,-1,-1],[0,0,0,1]])


mat.rep_type = cdd.RepType.INEQUALITY

poly = cdd.Polyhedron(mat)

print('ineq', poly.get_inequalities())
print('poly', poly)

print('poly.get_gen', poly.get_generators())


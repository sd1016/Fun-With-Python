A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print "Set A = {0}  Set B = {1}".format(A,B)
print "Set A union Set B = {0}".format(A.union(B))
print "Set A intersection Set B = {0}".format(A.intersection(B))
print "Set A difference Set B = {0}".format(A.difference(B))

"""
OUTPUT:
Set A = set([1, 2, 3, 4, 5])  Set B = set([8, 4, 5, 6, 7])
Set A union Set B = set([1, 2, 3, 4, 5, 6, 7, 8])
Set A intersection Set B = set([4, 5])
Set A difference Set B = set([1, 2, 3])
"""

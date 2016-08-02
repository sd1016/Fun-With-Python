# EXERCISE 10 from:
# http://www.practicepython.org/
#Python 2.7

#solution with given inputs
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print a
print b
print list(set([i for i in a for j in b if i == j]))

#solution by generating random lists
import random
a = []
b = []
#Generating two lists with random numbers ranging from 1 to 100
#with random size of 10-20
for i in range(random.randint(10,20)):
    a.append(random.randint(1,100))

for i in range(random.randint(10,20)):
    b.append(random.randint(1,100))

print"==========================================="
a.sort()
b.sort()
print a
print b
print list(set([i for i in a for j in b if i == j]))


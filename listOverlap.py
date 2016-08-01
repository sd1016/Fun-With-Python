# write a program that prints a list that
# contains only the elements that are common between the lists
# (without duplicates). Make sure your program
# works on two lists of different sizes.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
l = []

for i in list(set(a)):
 for j in list(set(b)):
  if(i == j):
   l.append(i)
print l

import random
a = []
b = []
for x in range(1,20):
    a.append(random.randint(1, 100))
a.sort()
print a

for y in range(1,20):
    b.append(random.randint(1,100))
b.sort()
print b

c = list(set(a).intersection(b))
c.sort()
print c






# EXERCISE 14 from:
# http://www.practicepython.org/
#Python 2.7

#Solution using a loop and constructing a list
def remv_dup(l):
    if not l:
        return []
    nl = []
    l.sort()
    temp = l[0]
    nl.append(temp)

    for i in l:
        if temp == i:
            continue
        temp = i
        nl.append(temp)
    return nl

print remv_dup([1,1,2,2,3,3,3,4,5,2,1,66,44,33,66,1,2,3,4,5,6])
print remv_dup([])
print remv_dup([1,1,2,22,3,3,11,11,55,2,11,66,44,33,66,1,2,3,4,555,6])
print remv_dup(["Apple","Bottle","Abhi","Zebra","Xerox","Ant"])


print "============================================="

# Solution using using sets
def dup_remv(l):
    return list(set(l))

print remv_dup([1,1,2,2,3,3,3,4,5,2,1,66,44,33,66,1,2,3,4,5,6])
print remv_dup([])
print remv_dup([1,1,2,22,3,3,11,11,55,2,11,66,44,33,66,1,2,3,4,555,6])
print remv_dup(["Apple","Bottle","Abhi","Zebra","Xerox","Ant"])



#Solution to http://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html

#store happy numbers in happylist:
with open("./temp-files/ex23-happy-nos.txt") as f:
    happylist = f.readlines()

#store prime numbers in primelist:
with open("./temp-files/ex23-prime-nos.txt") as f:
    primeslist = f.readlines()

#intersection of 2 lists
list3 = [elem.strip() for elem in primeslist if elem in happylist]

print (list3)
print (len(list3))



#one of official solutions:
def filetolistofints(filename):
    list_to_return = []
    with open(filename) as f:
        line = f.readline()
        while line:
            list_to_return.append(int(line))
            line = f.readline()
    return list_to_return

primeslist = filetolistofints('./temp-files/ex23-prime-nos.txt')
happieslist = filetolistofints('./temp-files/ex23-happy-nos.txt')

overlaplist = [elem for elem in primeslist if elem in happieslist]
print(overlaplist)
print (len(overlaplist))

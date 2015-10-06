import random
i = ""
count = 0
r = random.randint(1, 9)
while i.lower() != "exit":
    g = int(raw_input("Guess the integer between 1 and 9........."))
    if g == r:
        print "Correct!!!"
        count += 1
        print "The number of guesses=", count
        i = raw_input("Type in \"exit\" to stop this guessing game else press any letter or digit to continue ")
        r = random.randint(1, 9)
        count = 0
    else:
        print "Wrong :("
        count += 1
        if g > r:
            print "Guess is higher than the number"
        else:
            print "Guess is lower than the number"

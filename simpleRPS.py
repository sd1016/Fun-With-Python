import getpass
# This code runs best from the terminal
# Python 2.7 used

print "Welcome to Sid's simple implementation of Rock Paper Scissors"
print "Rules--->Rock beats Scissors//Scissors beats Paper//Paper beats Rock//Three rounds of guess per game"

user1 = raw_input("Player 1 please enter your name.....")
user2 = raw_input("Player 2 please enter your name.....")
run = 1
score1 = 0
score2 = 0
rounds = 0

while run == 1:

    inp1 = getpass.getpass(" %s enter your choice......." % user1)
    inp2 = getpass.getpass(" %s enter your choice......." % user2)
    inp1 = inp1.lower()
    inp2 = inp2.lower()
    if not (inp1 == "rock" or inp1 == "paper" or inp1 == "scissors"):
        print "%s has provided an invalid input....maybe check spelling (rock,paper,scissors)" % user1
        continue
    elif not (inp2 == "rock" or inp2 == "paper" or inp2 == "scissors"):
        print "%s has provided an invalid input....maybe check spelling (rock,paper,scissors)" % user2
        continue
    else:
        pass

    if inp1 == inp2:
        print "Its a tie"
        rounds += 1
    elif (inp1 == "rock" and inp2 == "paper") or (inp1 == "scissors" and inp2 == "rock") \
            or (inp1 == "paper" and inp2 == "scissors"):
        print "%s wins this round" % user2
        score2 += 1
        rounds += 1
    elif (inp2 == "rock" and inp1 == "paper") or (inp2 == "scissors" and inp1 == "rock") \
            or (inp2 == "paper" and inp1 == "scissors"):
        print "%s wins this round" % user1
        score1 += 1
        rounds += 1
    else:
        pass
    if rounds == 3 and score2 > score1:
        print "End of Round 3"
        print "%s WINS THIS GAME!!!!" % user2
        rounds = 0
        run = int(raw_input("Enter 0 to quit and 1 to start a new game"))
        if run:
            print "========NEW GAME======="
        continue

    elif rounds == 3 and score1 > score2:
        print "End of Round 3"
        print "%s WINS!!!!" % user1
        rounds = 0
        run = int(raw_input("Enter 0 to quit and 1 to start a new game"))
        if run:
            print "========NEW GAME======="
        continue
    elif rounds == 3 and score2 == score1:
        print "End of Round 3"
        print "This game ends in a tie!!!"
        rounds = 0
        run = int(raw_input("Enter 0 to quit and 1 to start a new game"))
        if run:
            print "========NEW GAME======="
        continue

    print "End of Round", rounds

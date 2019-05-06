import json

print ("\nWelcome to tito's Brirthday Dictionary Program\n\n")

with open("./temp-files/birthday-ex34.json","r") as f:
    bdays = json.load(f)
    print ("Following are the birthdays we have in our dictionary at the moment:\n")
    for key in bdays.keys():
        print ("{} {}".format(key,bdays[key]))

print ("Press 1 to add more brirthdays")
inp = int(input("---> "))
if inp==1:
    name = input("Enter name of person whose birthday you want to add ")
    dt = input("Enter birthday ")
    with open("./temp-files/birthday-ex34.json","r") as f:
        bdays = json.load(f)
        bdays[name] = dt
    with open("./temp-files/birthday-ex34.json","w") as f:
        json.dump(bdays,f)
    print ("\nBrirthday Dictionary  updated and Tito's Brirthday Dictionary Program Ended")

else:
    print ("\nTito's Brirthday Dictionary Program Ended")

#provided solution
#     import json
#
# birthday = {}
# with open('birthdays.json', 'r') as f:
#           birthday = json.load(f)
#
# def add_entry():
#     name = input('Who do you want to add to the Birthday Dictionnary?\n').title()
#     date = input('When is {} born?\n'.format(name))
#     birthday[name] = date
#     with open('birthdays.json', 'w') as f:
#         json.dump(birthday, f)
#     print('{} was added to my birthday list\n'.format(name))
#
# def find_date():
#     name = input("who's birthday do you want to know?\n").title()
#     try :
#         if birthday[name]:
#             print('{} is born on {}\n'.format(name, birthday[name]))
#     except KeyError:
#         print('{} is not in the list\n'.format(name))
#
# def list_entries():
#     print('The current entries in my birthday list are:\n============================================')
#     for key in birthday:
#         print(key.ljust(31), ':', birthday[key])
#     print()
#
# while True:
#     what_next = input('What do you want to do next? you can: Add, Find, List, Quit\n').capitalize()
#     if what_next == 'Quit':
#         print('Good Bye')
#         raise SystemExit(0)
#     elif what_next == 'Add':
#         add_entry()
#     elif what_next == 'Find':
#         find_date()
#     elif what_next == 'List':
#         list_entries()

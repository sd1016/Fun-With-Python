# EXERCISE 33 from:
# http://www.practicepython.org/
# Python 3.5

if __name__ == '__main__':
    birth_dict = {}
    inp = 1

    while inp:
        print ("Welcome to the birthday dictionary. We know the birthdays of:")
        print (birth_dict.keys())
        b = input("Who's birthday do you want to look up?")
        if b in birth_dict:
            print (birth_dict[b])
        else :
            print ("We dont have {}'s birthday information.".format(b))
            chck = int(input("Would you like to add {}'s birtday information? Type 1 to add else input any digit".format(b)))
            print (chck)
            if chck==1:
                dat = input("Enter Birthday for {}".format(b))
                birth_dict[b] = dat
        inp = int(input("Press 1 to continue else press 0 to abort."))



    #solution provided
    # if __name__ == '__main__':
    #
    # birthdays = {
    #     'Albert Einstein': '03/14/1879',
    #     'Benjamin Franklin': '01/17/1706',
    #     'Ada Lovelace': '12/10/1815',
    #     'Donald Trump': '06/14/1946',
    #     'Rowan Atkinson': '01/6/1955'}
    #
    # print('Welcome to the birthday dictionary. We know the birthdays of:')
    # for name in birthdays:
    #     print(name)
    #
    # print('Who\'s birthday do you want to look up?')
    # name = input()
    # if name in birthdays:
    #     print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    # else:
    #     print('Sadly, we don\'t have {}\'s birthday.'.format(name))

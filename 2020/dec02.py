
"""
    Advent of Code 2020 Day 2
    --- Day 2: Password Philosophy ---
    It's should be more secure than this...
    
"""
def passwordPolicies(passwords):
    """
        At his old firm, the passwords needed to contain a certain amount of a certain letter.
        Not more, not less, but exactly within the intervall.
        1-8 n: dpwpmhknmnlglhjtrbpx
    """
    returnedOldPasswords = []
    returnedNewPasswords = []
    for password in passwords:
        thisPassword = password[1].lstrip()
        thisPassword = thisPassword.rstrip()
        amountofchars = 0
        correctPass = False
        for chars in thisPassword:
            rules = password[0].split("-")
            rulelist = rules[1].split() #[0] index is maximum amount of chars, [1] index is the ruling character
            minchar = int(rules[0])
            maxchar = int(rulelist[0])
            rulechar = rulelist[1]
            if(chars == rulechar): amountofchars+=1
            

            """
                At this firm however, the password policy says that:
                "On these indexes, the character must be placed".
                Weird, but okay.
            """
            if(thisPassword[minchar-1] == rulechar):
                if(thisPassword[minchar-1] == thisPassword[maxchar-1]):
                    correctPass = False
                else:
                    correctPass = True
            elif(thisPassword[maxchar-1] == rulechar):
                if(thisPassword[minchar-1] == thisPassword[maxchar-1]):
                    correctPass = False
                else:
                    correctPass = True
        
        if(amountofchars >= minchar and amountofchars <= maxchar): returnedOldPasswords.append(thisPassword)
        if(correctPass): returnedNewPasswords.append(thisPassword)
    
    return returnedOldPasswords, returnedNewPasswords

def Main():
    """
        Each line gives the password policy and then the password. 
        The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. 
        For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

    """
    with open("adventofcode/2020/inputdec02.txt", "r") as f:
        puzzle_input = [line.split(":") for line in f.readlines()]

    correctPasswords = passwordPolicies(puzzle_input)
    print("Correct old passwords:", len(correctPasswords[0]), "\nCorrect current passwords:", len(correctPasswords[1]))
    #Prints 445 for part 1
    #Prints 491 for part 2






Main()



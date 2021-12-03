"""
    Advent of Code 2020 Day 1
    --- Day 1: Report Repair ---
    Time for some vacation...
    ...after some accounting...
    
"""

def importFile():
    inputList = []
    f = open("adventofcode/2020/inputdec01.txt", "rt") #Open inputfile, read and default text read
    #inputList = [int(opcode) for opcode in f.read().split(',')]
    inputList = [int(entry) for entry in f.readlines()]
    return inputList

def findTwoEntries(first, second):
    entrysum = first + second
    if(entrysum == 2020):
        return first*second
    else:
        return 0
def findThreeEntries(first, second, third):
    entrysum = first + second + third
    if(entrysum == 2020):
        return first*second*third
    else:
        return 0

def Main():
    puzzle_input = importFile()
    correctFirst = 0
    correctSecond = 0
    multipliedEntries = 0
    #part 1
    #Find two numbers in entries that sum is 2020
    #Return their product
    for i in puzzle_input:
        for j in puzzle_input:
            checkEntries = findTwoEntries(i, j)
            if(checkEntries != 0):
                correctFirst = i
                correctSecond = j
                multipliedEntries = findTwoEntries(i,j)
                break
            #print(multipliedEntries)
    print("Entries are:", correctFirst, correctSecond, "and their product is:", multipliedEntries)
    #471019

    #part 2
    #Find three numbers in entries that sum is 2020
    #Return their product
    p1 = 0
    p2 = 0
    p3 = 0
    prod3 = 0
    for i in puzzle_input:
        for j in puzzle_input:
            for k in puzzle_input:
                checkEntries = findThreeEntries(i,j,k)
                if(checkEntries != 0):
                    p1 = i
                    p2 = j
                    p3 = k
                    prod3 = findThreeEntries(i,j,k)
                    break
    print(p1, p2, p3, prod3)
    #103927824
Main()


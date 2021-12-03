#import math
import sys

lowest = sys.maxsize
wired = {}
stepwires = {}
def manhattanDistance(x, y):
    return abs(x) + abs(y)

def runWire(wires, check, part2):
    global lowest
    global wired
    global stepwires
    #print("Working on it.")
    x = 0
    y = 0
    steps = 0
    for path in wires:
        direction = path[0]
        distance = int(path[1:])
        xx = 0
        yy = 0
        if direction == "R": xx = 1
        if direction == "L": xx = -1
        if direction == "U": yy = 1
        if direction == "D": yy = -1

        for j in range(0, distance):
            x+=xx
            y+=yy
            steps+=1
            thispos = str(x)+"_"+str(y)
            if not part2:   #If part 1
                if(check):
                    #print("Hej")
                    if(wired.get(thispos) == 1):
                        #print("Hå")
                        dist = manhattanDistance(x,y)
                        if dist < lowest: lowest=dist
                else:
                    #print("Hallå?")    
                    wired[thispos] = 1


            else:           #If part 2
                if not(check):
                    wired[thispos]=1
                    if not(thispos in stepwires):
                        stepwires[thispos] = steps
                else:
                    if(wired.get(thispos) == 1):
                        dist = stepwires[thispos] + steps
                        if dist < lowest: lowest=dist







def Main():
    global lowest
    global wired
    global stepwires
    with open("adventofcode/2019/input03.txt", "r") as f:
        lines = [line.split(",") for line in f.read().split()]
    #Part 1
    runWire(lines[0], False, False)
    runWire(lines[1], True, False)
    print(lowest)
    input("Press Enter for part 2")
    #Part 2
    with open("adventofcode/2019/input03.txt", "r") as f:
        lines = [line.split(",") for line in f.read().split()]
    lowest=sys.maxsize
    wired = {}
    stepwires = {}
    runWire(lines[0], False, True)
    runWire(lines[1], True, True)
    print(lowest)


Main()